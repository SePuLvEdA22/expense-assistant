import os 
from telegram_ import run_bot
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN no configurado")
    
    run_bot(token)