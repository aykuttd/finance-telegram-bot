from telegram import Update
from telegram.ext import ContextTypes

async def financial_statement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/financial_statement' is issued."""
    await update.message.reply_text("""
        Menü yapım aşamasındadır.
    """)
