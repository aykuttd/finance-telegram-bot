from telegram import Update
from telegram.ext import ContextTypes
from utils import fetch


async def foreign_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/fx' is issued."""
    fx = {"TRY=X": "USD/TRY", "EURTRY=X": "EUR/TRY", "GBPTRY=X": "GBP/TRY", "TRYJPY=X": "TRY/JPY",
          "EURUSD=X": "EUR/USD",
          "GBPUSD=X": "GBP/USD", "JPY=X": "USD/JPY"}
    ticker = list(fx.keys())
    data = {}
    message = ""
    for t in ticker:
        prices = fetch(ticker=t)
        data[t] = prices
        message += f"{fx[t]}: {prices.iloc[-1]['Close']:.4f}\n"
    await update.message.reply_text(message)
