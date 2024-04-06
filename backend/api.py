from datetime import datetime
from os import getenv
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = FastAPI()
OPEN_API_KEY = getenv("OPEN_AI_KEY")
CHAT_BOT_BASE = "you are a chatbot for creating steps for a given query, please enumerate steps and separate" \
                " them with new lines."
BASE_QUERY = "Create a steps for "
client = OpenAI(api_key=OPEN_API_KEY)


class Prompt(BaseModel):
    text: str
    current_state: str
    steps: int


@app.post("/")
async def get_reply(prompt: Prompt):
    message = CHAT_BOT_BASE
    if prompt.steps:
        message += f" Use {prompt.steps} steps."

    if prompt.current_state:
        message += f"Current progress is {prompt.current_state}"

    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "system",
                                                         "content": message},
                                                        {"role": "user", "content": BASE_QUERY + prompt.text}])

    response_text = response.choices[0].message.content
    steps = response_text.split("\n")

    return {"steps": steps, "number_of_steps": len(steps), "created": datetime.now()}
