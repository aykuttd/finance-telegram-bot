from enum import Enum

__all__ = (
    "start",
    "info",
    "analyze",
    "financial_statement",
    "foreign_exchange",
    "markets",
    "news",
    "stocks",
    "crypto",
    "command_handlers"
)


from .start import start
from .info import info
from .analyze import analyze
from .financial_statement import financial_statement
from .foreign_exchange import foreign_exchange
from .markets import markets
from .news import news
from .stocks import stock
from .crypto import crypto

command_handlers = {
    "start": start,
    "info": info,
    "fx": foreign_exchange,
    "markets": markets,
    "stock": stocks,
    "fs": financial_statement,
    "analyze": analyze,
    "crypto": crypto,
    "news": news
}
