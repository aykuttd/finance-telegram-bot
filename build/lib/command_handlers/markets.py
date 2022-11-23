from telegram import Update
from telegram.ext import ContextTypes
from utils import fetch


async def markets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/market_index' is issued."""
    borsalar = {"XU100.IS": "BIST100", "^GSPC": "S&P 500", "^DJI": "Dow 30", "^IXIC": "Nasdaq", "^N225": "Nikkei 225",
                "^GDAXI": "DAX PERFORMANCE-INDEX", "IMOEX.ME": "MOEX Russia Index", "^BVSP": "IBOVESPA"}
    ticker = list(borsalar.keys())
    data = {}
    message = ""
    for t in ticker:
        prices = fetch(ticker=t)
        data[t] = prices
        message += f"{borsalar[t]}: {prices.iloc[-1]['Close']:.2f}\n"
    await update.message.reply_text(message)