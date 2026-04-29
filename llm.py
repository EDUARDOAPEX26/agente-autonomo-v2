# llm.py

def generate(prompt, mode="default", model="cloud"):
    """
    LLM offline (stub) para manter o sistema funcionando sem APIs.
    """

    if not prompt:
        return "Entrada vazia."

    texto = prompt.lower().strip()

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
# RESPOSTAS CURTAS
# ------------------------

def _resposta_curta(texto):
    if "python" in texto:
        return "Python é uma linguagem de programação."

    if _tem_calculo(texto):
        return _resolver_calculo(texto)

    return "Não tenho resposta curta para isso."


# ------------------------
# RESPOSTAS LONGAS
# ------------------------

def _resposta_longa(texto):
    if "python" in texto:
        return (
            "Python é uma linguagem de programação de alto nível, conhecida por sua "
            "simplicidade e legibilidade. Ela é usada em diversas áreas como "
            "automação, desenvolvimento web, análise de dados e inteligência artificial."
        )

    return (
        "Esta é uma resposta simulada em modo longo. "
        "Em um ambiente completo, um modelo de linguagem geraria uma explicação detalhada."
    )


# ------------------------
# RESPOSTA PADRÃO
# ------------------------

def _resposta_padrao(texto):
    if "python" in texto:
        return "Python é uma linguagem usada para programar."

    if "oi" in texto or "olá" in texto:
        return "Olá! Como posso ajudar?"

    if _tem_calculo(texto):
        return _resolver_calculo(texto)

    return "Resposta simulada (LLM offline)."


# ------------------------
# UTILIDADES
# ------------------------

def _tem_calculo(texto):
    return any(op in texto for op in ["+", "-", "*", "/"])


def _resolver_calculo(texto):
    try:
        return str(eval(texto))
    except:
        return "Erro ao calcular."
