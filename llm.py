import os
import requests


def generate(prompt, mode="default", model="cloud"):

    if not prompt or not isinstance(prompt, str):
        return "Entrada inválida."

    resposta = usar_groq(prompt)

    return resposta


def usar_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "ERRO: GROQ_API_KEY não encontrada no ambiente"

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)

        # DEBUG STATUS
        if r.status_code != 200:
            return f"ERRO HTTP: {r.status_code} | {r.text}"

        res = r.json()

        # DEBUG ERRO DA API
        if "error" in res:
            return f"ERRO GROQ: {res['error']}"

        # RESPOSTA NORMAL
        return res["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERRO EXCEPTION: {str(e)}"
