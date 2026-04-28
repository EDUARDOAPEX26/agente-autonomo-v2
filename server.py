from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# modelo de entrada (melhor que dict)
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
    texto = req.text

    # resposta simples (por enquanto)
    resposta = f"recebi: {texto}"

    return {
        "response": resposta
    }
