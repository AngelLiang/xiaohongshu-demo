import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from services import ChatClient
from dotenv import load_dotenv
load_dotenv()

SPARK_APPID = os.getenv('SPARK_APPID', None)
SPARK_APISECRET = os.getenv('SPARK_APISECRET', None)
SPARK_APIKEY = os.getenv('SPARK_APIKEY', None)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


class GenerateIn(BaseModel):
    prompt: str


@app.post('/api/generate')
async def generate(payload: GenerateIn):
    prompt = payload.prompt
    stream = ChatClient(SPARK_APIKEY, SPARK_APISECRET).generate(
        prompt, stream=True)
    return StreamingResponse(stream)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")
