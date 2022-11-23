from telegram import Update
from telegram.ext import ContextTypes

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/news' is issued."""
    await update.message.reply_text("""
        Menü yapım aşamasındadır.
    """)
