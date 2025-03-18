import pandas as pd
from binance.um_futures import UMFutures
from .dataTypes import Candlestick

def processRawCandlestickData(rawCD: list):
    #Transforms raw data from Binance kline API to Candlestick type
    return [
        Candlestick(
            Date = pd.Timestamp(cd[0], unit='ms'),
            Open = cd[1],
            High = cd[2],
            Low = cd[3],
            Close = cd[4],
            Volume = cd[5],
        )
        for cd in rawCD
    ]

def getPastCandlesDF(pair, timeframe):
    #Request Binance API kline data and returns a Pandas DataFrame with Candlesticks
    um_futures_client = UMFutures()
    pastCandleSticks = um_futures_client.klines(pair, timeframe, limit=1000)
    df = Candlestick.makeCandlestickDataFrame(processRawCandlestickData(pastCandleSticks))
    
    #Format 'Date' to be the DataFrame index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df