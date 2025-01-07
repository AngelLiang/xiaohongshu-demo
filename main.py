import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import StreamingResponse, Response
from services import ChatClient
from dotenv import load_dotenv
load_dotenv()

OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL', '')
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY', '')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', '')

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


class GenerateIn(BaseModel):
    prompt: str
    stream: bool


@app.post('/api/generate')
def generate(payload: GenerateIn):
    prompt = payload.prompt
    is_stream = payload.stream
    chat_client = ChatClient(OPENAI_BASE_URL, OPENAI_APIKEY, OPENAI_MODEL)
    if is_stream:
        generator = chat_client.generate_stream(prompt)
        return StreamingResponse(generator)
    else:
        response = chat_client.generate(prompt)
        return Response(response)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")
