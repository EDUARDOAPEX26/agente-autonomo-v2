# llm.py

def generate(prompt, mode="default", model="cloud"):
    """
    LLM offline (stub) para manter o sistema funcionando sem APIs.
    """

    texto = prompt.lower()

    # ------------------------
    # MODO SHORT
    # ------------------------
    if mode == "short":
        return _resposta_curta(texto)

    # ------------------------
    # MODO LONG
    # ------------------------
    if mode == "long":
        return _resposta_longa(texto)

    # ------------------------
    # DEFAULT
    # ------------------------
    return _resposta_padrao(texto)


# ------------------------
# RESPOSTAS
# ------------------------

def _resposta_curta(texto):
    if "python" in texto:
        return "Python é uma linguagem de programação."

    if any(op in texto for op in ["+", "-", "*", "/"]):
        try:
            return str(eval(texto))
        except:
            return "Erro no cálculo."

    return "Resposta curta não disponível."


def _resposta_longa(texto):
    if "python" in texto:
        return (
            "Python é uma linguagem de programação de alto nível, "
            "conhecida por sua simplicidade e legibilidade. "
            "Ela é amplamente usada em automação, desenvolvimento web, "
            "ciência de dados e inteligência artificial."
        )

    return (
        "Esta é uma resposta simulada em modo longo. "
        "Em um ambiente completo, um modelo de linguagem geraria "
        "uma explicação detalhada aqui."
    )


def _resposta_padrao(texto):
    if "python" in texto:
        return "Python é uma linguagem usada para programar."

    return "Resposta simulada (LLM offline)."
