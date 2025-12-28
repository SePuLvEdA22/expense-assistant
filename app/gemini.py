import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.client(
    api_key = os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-1.5-pro"

CATEGORIES = [
    "comida",
    "transporte",
    "servicios_domesticos",
    "entretenimiento",
    "salud",
    "otros"
]

def classify_expense(text: str) -> dict:
    prompt = f"""
        Analyze the following expense text and return ONLY a valid JSON 
        with the exact schema below.
        
        Schema: 
        {{
            "amount": number,
            "category": one of {CATEGORIES},
            "description": string
        }}
        
        Text:
        \"{text}\"
    """
    
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        
        return json.loads(response.text)
    
    except Exception as e:
       print(f"Gemini error: {e}")
       return {} 