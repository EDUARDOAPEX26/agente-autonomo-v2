# llm.py

import re


def generate(prompt, mode="default", model="cloud"):
    """
    LLM offline (stub) para manter o sistema funcionando sem APIs.
    Compatível com pipeline do Agent V2.
    """

    if not prompt or not isinstance(prompt, str):
        return "Entrada inválida."

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


# ========================
# RESPOSTAS CURTAS
# ========================

def _resposta_curta(texto):
    if "python" in texto:
        return "Python é uma linguagem de programação."

    if _tem_calculo(texto):
        return _resolver_calculo(texto)

    if _is_saudacao(texto):
        return "Olá!"

    return "Não tenho resposta curta para isso."


# ========================
# RESPOSTAS LONGAS
# ========================

def _resposta_longa(texto):
    if "python" in texto:
        return (
            "Python é uma linguagem de programação de alto nível, conhecida por sua "
            "simplicidade e legibilidade. Ela é amplamente utilizada em automação, "
            "desenvolvimento web, ciência de dados e inteligência artificial. "
            "Sua sintaxe clara facilita o aprendizado e a manutenção de código."
        )

    if _is_saudacao(texto):
        return "Olá! Posso te ajudar com dúvidas, cálculos ou explicações simples."

    return (
        "Esta é uma resposta simulada em modo longo. "
        "O sistema está operando sem um modelo de linguagem real neste ambiente."
    )


# ========================
# RESPOSTA PADRÃO
# ========================

def _resposta_padrao(texto):
    if "python" in texto:
        return "Python é uma linguagem usada para programar."

    if _is_saudacao(texto):
        return "Olá! Como posso ajudar?"

    if _tem_calculo(texto):
        return _resolver_calculo(texto)

    if "explique" in texto or "o que é" in texto:
        return "Posso dar uma explicação básica, mas este ambiente está sem LLM completo."

    return "Resposta simulada (LLM offline)."


# ========================
# UTILIDADES
# ========================

def _tem_calculo(texto):
    return any(op in texto for op in ["+", "-", "*", "/"])


def _resolver_calculo(texto):
    try:
        # Mantém apenas caracteres seguros
        expressao = re.sub(r"[^0-9\+\-\*\/\.\(\) ]", "", texto)

        if not expressao.strip():
            return "Erro ao calcular."

        return str(eval(expressao))
    except:
        return "Erro ao calcular."


def _is_saudacao(texto):
    return any(p in texto for p in ["oi", "olá", "ola", "hello", "hi"])
