from telegram import Update
from telegram.ext import ContextTypes

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/analyze' is issued."""
    await update.message.reply_text("""
        /capm -> Sermaye Varlıkları Fiyatlama Modeli (Hisse senedinin yüksek ya da az değer biçildiğini ölçmek amacıyla oluşturulan benchmark modelidir.).
        /pddd -> Piyasa Değeri/Defter Değeri Rasyosu.
        /fk   -> Fiyat/Kar Rasyosu.

    """)