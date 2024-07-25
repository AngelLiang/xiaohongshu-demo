import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return 'hello'


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")
