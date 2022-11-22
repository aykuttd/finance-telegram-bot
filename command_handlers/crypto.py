from telegram import Update
from telegram.ext import ContextTypes
from utils import fetch


async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/kripto' is issued."""
    cry = {"BTC-USD": "BTC/USD", "ETH-USD": "ETH/USD", "BNB-USD": "BNB/USD", "XRP-USD": "XRP/USD", "ADA-USD": "ADA/USD",
           "DOGE-USD": "DOGE/USD", "MATIC-USD": "MATIC/USD", "DOT-USD": "DOT/USD", "TRX-USD": "TRX/USD",
           "SHIB-USD": "SHIB/USD"}
    ticker = list(cry.keys())
    data = {}
    message = ""
    for t in ticker:
        prices = fetch(ticker=t)
        data[t] = prices
        message += f"{cry[t]}: {prices.iloc[-1]['Close']:.9f}\n"
    await update.message.reply_text(message)
