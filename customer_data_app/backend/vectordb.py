import google.generativeai as genai
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import os

TEXT_SUMMARY_PROMPT = """You are an assistant tailored for summarizing text for retrieval.
These summaries will be turned into vector embeddings and used to retrieve the raw text.
Give a concise summary of the text that is well optimized for retrieval. Here is the text."""

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel('models/gemini-1.5-flash', safety_settings=safety_settings)

chroma_client = chromadb.PersistentClient()

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        model = 'models/text-embedding-004'
        title = "Custom query"
        return genai.embed_content(model=model,
                                    content=input,
                                    task_type="retrieval_document",
                                    title=title)["embedding"]

def create_chroma_db(name: str):
    db = chroma_client.get_or_create_collection(name=name, embedding_function=GeminiEmbeddingFunction())
    return db

def create_text_summary(text: str) -> str:
    response = model.generate_content([TEXT_SUMMARY_PROMPT, text])

    return response.text

def add_to_chroma_db(db: chromadb.Collection, note_content: str, random_id: str) -> None:
    summary = create_text_summary(note_content)

    db.add(
        documents=[summary],
        ids=random_id
    )

def get_relevant_files(query: str, db: chromadb.Collection) -> list[str] | None:
    results = db.query(query_texts=[query], n_results=1)
    if results["distances"][0][0] >= 0.7:
        return None
    return results["ids"][0]

# def query_rag(query, db):
#     files = get_relevant_files(query, db)
#     prompt = [all_files[int(f)] for f in files]
#     prompt.append("Generate a response to the query using the provided files. Here is the query.")
#     prompt.append(query)
#     return model.generate_content(prompt).text, [all_file_names[int(f)] for f in files]
