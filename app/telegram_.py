from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    await update.message.reply_text(
        f"Recibido \nText: {user_text}"
    )
    
def run_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    
    print("🤖 Bot corriendo...")
    app.run_polling()



