import re
from datetime import date

COMMON_WORDS = [
    "gaste", "gasté", "en", "el", "la", "los", "las", "un", "una", "unos", "unas"
]

def normalize_text(text: str) -> str:
    return text.lower().strip() # Elimina espacios en blanco al inicio y al final

def extract_amount(text: str) -> str | None:
    """
        - re.search(): busca un patrón en el texto
        - r"\d+": expresión regular que significa:
        - \d: cualquier dígito (0-9)
        - +: uno o más dígitos consecutivos
        - Encuentra la primera secuencia de números en el texto
    """
    match = re.search(r"\d+", text.replace(".", ""))
    """
        - match será None si no hay números, o un objeto Match si los hay
        - match.group(): obtiene el texto que coincidió (el número como string)
    """
    if match:
        return int(match.group())
    return None

def extract_description(text: str) -> str:
    words = normalize_text(text).split() # Divide un string en una ccadena de substrings usando un separador
    
    filtered = [
        w for w in words
        if w not in COMMON_WORDS and not w.isdigit()
    ]
    
    return " ".join(filtered)  # une todos los elementos de la lista en un solo string. Los separa con un espacio " "
    
def parse_expense(text: str) -> dict:
    amount = extract_amount(text)
    description = extract_description(text)
    
    return {
        "amount": amount,
        "description": description,
        "date": date.today().isoformat()
    }
    