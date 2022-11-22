from telegram import Update
from telegram.ext import ContextTypes
from utils import fetch


async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/stock' is issued."""
    ticker = context.args[0]
    data = fetch(ticker=ticker)
    price = data.iloc[-1]['Close']
    await update.message.reply_text(f"{ticker} için son fiyat; {price:.2f}")
