import uuid
import reflex as rx
import threading
import asyncio
from typing import Optional
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)
from sqlmodel import select, asc, desc, or_, func, cast, String, Field
from datetime import datetime, timedelta
from .vectordb import create_chroma_db, add_to_chroma_db, get_relevant_files
from .const import NOTE_1_CONTENT, NOTE_2_CONTENT, NOTE_3_CONTENT
import os
from groq import Groq
#LiteralStatus = Literal["Delivered", "Pending", "Cancelled"]

vector_db = create_chroma_db("Notes")
dg_connection = None
microphone: Optional[Microphone] = None
_recording_task = None
transcript = ""
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class User(rx.Model, table=True):
    """The user model."""

    name: str
    email: str
    phone: str


class Note(rx.Model, table=True):
    """The note model."""
    uuid: str = Field(primary_key=True)
    name: str
    content: str # is there a way to represent like latex here or smth
    date: str
    course_id: str


class State(rx.State):
    """The app state."""

    notes: list[Note] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_note: Note = Note()
    document_content: str = ""
    selected_note: Note = Note()
    is_streaming: bool = False
    recording: bool = False

    # def __init__(self):
    #     super().__init__()
        # self.vector_db = create_chroma_db("Notes")
    # semantic search for test
    search_query: str = ""
    search_results: list[str] = []
    show_dialog: bool = False

    def perform_search(self):
        # Simulating a search function. Replace this with your actual search logic.
        results = get_relevant_files(self.search_query, vector_db)

        # self.search_results = [f"Result {i} for '{self.search_query}'" for i in range(1, 6)]
        self.search_results = [f"{results[0]}"]
        self.show_dialog = True

    def select_note(self, note):
        self.selected_note = note

    def close_dialog(self):
        self.show_dialog = False

    def start_streaming(self, _ev=None):
        self.is_streaming = True
        # In a real implementation, you would set up an async task to stream content
        # For demonstration, we'll just update the content after a delay
        yield rx.set_timeout(1, self.update_content("Initial content\n"))
        yield rx.set_timeout(2, self.update_content("More content\n"))
        yield rx.set_timeout(3, self.update_content("Final content"))
        yield rx.set_timeout(4, self.stop_streaming())

    def update_content(self, new_content: str):
        self.document_content += new_content
    
    def set_content(self, new_content: str):
        self.document_content = new_content

    def stop_streaming(self):
        self.is_streaming = False

    def load_entries(self) -> list[Note]:
        """Get all notes from the database."""
        with rx.session() as session:
            query = select(Note)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Note, field).ilike(search_value)
                            for field in Note.get_fields()
                            if field not in ["id"]
                        ]
                    )
                )

            if self.sort_value:
                sort_column = getattr(Note, self.sort_value)
                order = desc(func.lower(sort_column)) if self.sort_reverse else asc(func.lower(sort_column))
                query = query.order_by(order)
            
            self.notes = session.exec(query).all()


    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()


    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def toggle_recording(self):
        # print("DEBUG1")
        self.recording = not self.recording
        if self.recording:  
            return State.start_recording()
        else:
            return State.stop_recording()

    @rx.background
    async def start_recording(self):
        global dg_connection, microphone
        if dg_connection is not None:
            return

        try:
            deepgram: DeepgramClient = DeepgramClient()
            dg_connection = deepgram.listen.websocket.v("1")

            def on_message(self, result, **kwargs):
                global transcript
                sentence = result.channel.alternatives[0].transcript
                if result.is_final:
                    # print("DEBUG3")
                    transcript += sentence + " "
                    # print(transcript)
                    # breakpoint()
                    # State.update_transcript(sentence)
                    # asyncio.create_task(State.update_transcript(sentence))
                    # print("DEBUG4")

            dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)

            options = LiveOptions(
                model="nova-2",
                language="en-US",
                smart_format=True,
                encoding="linear16",
                channels=1,
                sample_rate=16000,
                # interim_results=True,
                # utterance_end_ms="1000",
                # vad_events=True,
                # endpointing=300,
            )
            addons = {
                # Prevent waiting for additional numbers
                "no_delay": "true"
            }


            if dg_connection.start(options, addons=addons) is False:
                print("Failed to connect to Deepgram")
                return

            microphone = Microphone(dg_connection.send)
            microphone.start()
            while self.recording:
                await asyncio.sleep(0.1)

        except Exception as e:
            print(f"Could not open socket: {e}")
            
    @rx.background
    async def stop_recording(self):
        global dg_connection, microphone
        async with self:
            self.recording = False
            if microphone:
                microphone.finish()
            if dg_connection:
                dg_connection.finish()
            microphone = None
            dg_connection = None
            
            self.update_notes(transcript)

    def update_notes(self, transcript: str):
        """Returns additional information added to note."""
        results = get_relevant_files(transcript, vector_db)
        uuid = results[0]

        note = self.get_note_by_uuid(uuid)

        if not note:
            raise Exception("Note not found.")
        
        self.select_note(note)
        
        # summary = self.summarize_transcript(transcript)

        note_with_locations = ""
        lines = [line for line in note.content.split('\n') if line.strip()]
        index = 0
        for line in lines:
            note_with_locations += line + '\n' + str(index) + '\n'
            index += 1

        # print("summary: ", summary)

        # print("old_content: ", note.content)

        location, rewritten_summary  = self.location_and_new_content(note_with_locations, transcript)

        new_content = ""
        index = 0
        for line in lines:
            new_content += line + '\n' + '\n'
            index += 1
            if index == location:
                new_content += rewritten_summary + '\n' + '\n'

        # print("new_content: ", new_content)

        with rx.session() as session:
            curr_note = session.exec(select(Note).where(Note.uuid == uuid)).first()
            curr_note.content = new_content
            session.add(curr_note)
            session.commit()

        return rewritten_summary

        # self.update_note_to_db(new_note)
        
        # use groq and chatgpt to summarize the important information in transcript. then, figure out which line of note we should add it to, then return the entire note with the new information added.

    # def summarize_transcript(self, transcript: str) -> str:
    #     messages = [
    #         {
    #             "role": "system", 
    #             "content": "You are an assistant that summarizes a transcript"
    #         },
    #         {
    #             "role": "user", 
    #             "content": f"{transcript}"
    #         }
    #     ]
        
    #     chat_completion = client.chat.completions.create(
    #         messages=messages,
    #         model="llama3-70b-8192",
    #     )

    #     print("DEBUG", chat_completion.choices[0].message.content)

    #     return chat_completion.choices[0].message.content
    
    def location_and_new_content(self, note_with_locations: str, new_info: str) -> tuple:
        messages = [
            {
                "role": "system", 
                "content": (
                    """You are an assistant that is given a note page for a class with a number between 
                    each paragraph, and new information. Your task is to determine which 
                    number is the most suitable location in the note page to add the new information. 
                    Additionally, you must synthesize and rewrite the new information in Github-flavored markdown to fit 
                    seamlessly into the note's existing content. Return both the number and the rewritten 
                    new information in markdown, separated by a delimiter '###'. Pay attention to and include necessary 
                    spacing, punctuation, and symbols for the Github-flavored markdown text."""
                )
            },
            {
                "role": "user", 
                "content": (
                    f"""
                    Here's an example of the inputs and outputs, ensure your output conforms to the same format.

                    INPUTS:
                    Input 1: note page with locations
                    ## Why is the Internet Interesting?
                    0
                    - **New problem**: Tying together different, existing networks
                    1
                    - **Challenges**:
                    2
                      - No formal model
                    3
                      - No measurable performance benchmark
                    4
                      - Must scale to **billions** of users
                    5
                      - Must align with business relationships
                    6

                    Input 2: new information
                    Federation enables the tremendous scale of the Internet. Instead of a single operator managing billions of users and trillions of services, we only need to focus on interconnecting all the different operators. Federation also allows us to build the Internet out of a huge diversity of technologies (e.g. wireless, optical), with a huge range of capabilities (e.g. home links with tiny capacity, or undersea cables with huge capacity). These technologies are also constantly evolving, which means we can't aim for a fixed target (e.g. capacity and demand is constantly increasing by orders of magnitude). The massive scale of the Internet also means that any system we design has to support the massive range of users and applications on the Internet (e.g. some need more capacity than others, some may be malicious).

                    EXPECTED OUTPUT (do NOT output this portion, just the below line):
                    4###  - Support a massive range of users and applications

                    Use the new information: {new_info}, and the existing note page with 
                    locations: {note_with_locations} to form your output."""
                )
            },
        ]
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-70b-8192",
        )

        output = chat_completion.choices[0].message.content

        print("LLM_OUTPUT", output)

        if "###" not in output:
            raise Exception("Output does not contain the expected delimiter '###'.")

        # Split the output into the location number and the rewritten summary
        location, rewritten_summary = output.split("###", 1)

        # print(location)

        if not location.isdigit():
            raise Exception("The location part is not a valid number.")

        return int(location), rewritten_summary

    
    # def insert_summary_into_note(self, note_content: str, summary: str) -> str:
    #     messages = [
    #         {
    #             "role": "system", 
    #             "content": "You are an assistant that is given a note page for a class, and a summary of new information. Figure out where in the note page we should add it to, then return the entire note page with the new information added."
    #         },
    #         {
    #             "role": "user", 
    #             "content": f"Here's the new information {summary}, and here's the existing note page {note_content}"
    #         }
    #     ]
        
    #     chat_completion = client.chat.completions.create(
    #         messages=messages,
    #         model="llama3-70b-8192",
    #     )

    #     return chat_completion.choices[0].message.content

    def get_note_by_uuid(self, note_uuid: str) -> Optional[Note]:
        """Retrieve a note based on its UUID."""
        with rx.session() as session:
            note = session.exec(select(Note).where(Note.uuid == note_uuid)).first()
            return note


    def add_note_to_db(self, form_data: dict):
        random_id = str(uuid.uuid4())

        self.current_note = form_data
        self.current_note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_note["uuid"] = random_id

        with rx.session() as session:
            if session.exec(
                select(Note).where(Note.name == self.current_note["name"])
            ).first():
                return rx.window_alert("Note with this name already exists")
            note = Note(**self.current_note)
            # print(note.uuid)
            session.add(note)
            session.commit()
        self.load_entries()

        add_to_chroma_db(vector_db, self.current_note["content"], random_id)

        # print(vector_db.count())

        # Create link between randomized chroma db and postgres id

        return rx.toast.info(f"Note {self.current_note['name']} has been added.", position="bottom-right")
    
    def update_note_to_db(self, form_data: dict):
        self.current_note.update(form_data)
        with rx.session() as session:
            note = session.exec(
                select(Note).where(Note.uuid == self.current_note["uuid"]) # Might need to be uuid now
            ).first()
            for field in Note.get_fields():
                if field != "id":
                    setattr(note, field, self.current_note[field])
            session.add(note)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Note {self.current_note['name']} has been modified.", position="bottom-right")


    def delete_note(self, name: str):
        """Delete a note from the database."""

        note_id = None

        with rx.session() as session:
            note = session.exec(select(Note).where(Note.name == name)).first()
            note_id = note.uuid
            session.delete(note)
            session.commit()
        self.load_entries()

        if note_id:
            vector_db.delete(ids=[note_id])

        return rx.toast.info(f"Note {note.name} has been deleted.", position="bottom-right")
    # @rx.var
    # def payments_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.total_payments, self.previous_month_values.total_payments)

    def create_sample_notes(self):
        now = datetime.now()

        note_1 = {"name": "Introduction to the Internet", 
                  "content": NOTE_1_CONTENT, 
                  "date": datetime(now.year, now.month, 1), 
                  "course_id": "Networking 101"}
        note_2 = {"name": "Router Hardware", 
                  "content": NOTE_2_CONTENT, 
                  "date": datetime(now.year, now.month, 5), 
                  "course_id": "Networking 101"}
        note_3 = {"name": "Resource Sharing", 
                  "content": NOTE_3_CONTENT, 
                  "date": datetime(now.year, now.month, 11), 
                  "course_id": "Networking 101"}
        
        self.add_note_to_db(note_1)
        self.add_note_to_db(note_2)
        self.add_note_to_db(note_3)

        # add_to_chroma_db(vector_db, "Introduction to the Internet" + NOTE_1_CONTENT)
        # add_to_chroma_db(vector_db, "Router Hardware" + NOTE_2_CONTENT)
        # add_to_chroma_db(vector_db, "Cellular Technologies" + NOTE_3_CONTENT)
