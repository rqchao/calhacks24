import asyncio
import reflex as rx
from typing import List
from groq import Groq
import os
from celery import Celery

class State(rx.State):
    transcript: str = ""
    bullets: List[str] = []
    poll_interval: int = 5  # default to 5 seconds

    async def process_transcript(self):
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        celery_app = Celery('tasks', broker='your_broker_url')

        while True:
            # This would be replaced with your actual speech-to-text function
            new_transcript = await self.get_new_transcript()  

            if new_transcript != self.transcript:
                self.transcript = new_transcript

                # Process with Groq
                messages = [
                    {
                        "role": "system", 
                        "content": "You are an assistant that summarizes transcripts into bullet points. If the new content is relevant to the last bullet point, modify it. If it's new information, create a new bullet point."
                    },
                    {
                        "role": "user", 
                        "content": f"Current bullet points: {self.bullets}\nNew transcript: {self.transcript}"
                    }
                ]

                chat_completion = client.chat.completions.create(
                    messages=messages,
                    model="llama-3.2-11b-vision-preview",
                )

                new_bullets = chat_completion.choices[0].message.content.split('\n')

                if len(new_bullets) > len(self.bullets):
                    # A new bullet point was added
                    new_bullet = new_bullets[-1]
                    self.bullets.append(new_bullet)

                    # Trigger Celery task with new state
                    celery_app.send_task('update_task', args=[self.bullets[:-1]])
                else:
                    # Update the last bullet point
                    self.bullets[-1] = new_bullets[-1]

            await asyncio.sleep(self.poll_interval)

    async def get_new_transcript(self):
        # This is a placeholder for your speech-to-text function
        # Replace this with your actual implementation
        return "New transcript content"

    def set_poll_interval(self, interval: int):
        self.poll_interval = interval