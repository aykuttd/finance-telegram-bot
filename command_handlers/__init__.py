__all__ = (
    "start",
    "info",
    "analyze",
    "financial_statement",
    "foreign_exchange",
    "markets",
    "news",
    "stock",
    "crypto",
    "handlers",
    "error_handler"
)


from .start import start
from .info import info
from .analyze import analyze
from .financial_statement import financial_statement
from .foreign_exchange import foreign_exchange
from .markets import markets
from .news import news
from .stock import stock
from .crypto import crypto
from .error_handler import error_handler

handlers = {
    "start": start,
    "info": info,
    "fx": foreign_exchange,
    "markets": markets,
    "stock": stock,
    "fs": financial_statement,
    "analyze": analyze,
    "crypto": crypto,
    "news": news
}
