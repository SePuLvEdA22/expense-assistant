from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from parser import parse_expense

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user_text = update.message.text
    expense = parse_expense(user_text)
    
    if not expense["amount"]:
        await update.message.reply_text("No se pudo detectar el monto")
        return
    
    response = (
        "Registrado \n"
        f"Amount: {expense['amount']} COP \n"
        f"Description: {expense['description']}\n"
        f"Date: {expense['date']}"
    )
    
    await update.message.reply_text(response)
    
def run_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    
    print("🤖 Bot corriendo...")
    app.run_polling()



