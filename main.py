
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я DoDepBot.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token("PASTE_YOUR_BOT_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
