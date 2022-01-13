import yfinance as yf
from datetime import date

today = date.today()


def get_assets(ticker, start=(today)):
    hist = yf.download(ticker, start=start, interval="1d",)
    value_close = hist['Adj Close']
    return value_close


portifolio = [
    {
        "ticker": "PETR4.SA",
        "start": today

    },
    {
        "ticker": "ITSA4.SA",
        "start": today
    },
    {
        "ticker": "ITUB3.SA",
        "start": today
    },
    {
        "ticker": "ITUB3.SA",
        "start": today
    },
    {
        "ticker": "MXRF11.SA",
        "start": today
    }
]


def calculate_atives(wallet):
    resultado = []
    COLS = ('ticker')
    if len(wallet) > 0:
        for actives in wallet:
            hist = get_assets(ticker=actives['ticker'], start=actives['start'])
            hist = hist.reset_index()
            hist = hist.rename(columns={'Date': 'data'})
            resultado.append(
                {
                    actives['ticker']: hist
                }
            )
    return resultado
