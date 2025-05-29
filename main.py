from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI  # ← FIXED
import os

load_dotenv()
base_url = os.getenv("BASE_URL")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        client = OpenAI(base_url=base_url)  # uses OPENAI_API_KEY from env
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": req.message}
            ]
        )
        reply = response.choices[0].message.content  # ← FIXED
        return {"reply": reply}
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return {"reply": f"Error: {e}"}
