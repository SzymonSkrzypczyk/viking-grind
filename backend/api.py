from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = FastAPI()
client = OpenAI()
OPEN_API_KEY = ""


@app.post("/")
async def get_reply():
    ...
