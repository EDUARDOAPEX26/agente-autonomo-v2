from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate

app = FastAPI()


# modelo de entrada
class Request(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "status": "online",
        "agente": "v2"
    }


@app.get("/ping")
def ping():
    return {"msg": "pong"}


@app.post("/think")
def think(req: Request):
    resposta = generate(req.text)

    return {
        "response": resposta
    }
