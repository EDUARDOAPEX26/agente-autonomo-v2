import os
import requests


def generate(prompt, mode="default", model="cloud"):

    if not prompt or not isinstance(prompt, str):
        return "Entrada inválida."

    # tenta usar LLM real
    resposta = _usar_groq(prompt)

    if resposta:
        return resposta

    # fallback se falhar
    return _fallback(prompt)


# =========================
# GROQ (LLM REAL)
# =========================

def _usar_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

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
        r = requests.post(url, headers=headers, json=data, timeout=15)
        res = r.json()

        return res["choices"][0]["message"]["content"]

    except Exception:
        return None


# =========================
# FALLBACK
# =========================

def _fallback(prompt):
    return f"(modo offline) recebi: {prompt}"
