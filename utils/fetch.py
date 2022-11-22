import pandas as pd
import pandas_datareader.data as web


def fetch(ticker: str) -> pd.DataFrame:
    return web.DataReader(name=ticker, data_source="yahoo", start="2022-11-20")