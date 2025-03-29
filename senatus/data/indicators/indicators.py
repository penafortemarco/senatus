import pandas as pd
from .. import PriceSeries, MetricSeries
from .utils import (
    calcRSI, 
    calcWRSI,
)

def getMAV(ps: PriceSeries, period: int = 20):
    df = ps.candles
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': df['close'].rolling(window=period).mean()
    }).set_index('timestamp'), ps.timeframe)

def getEMA(ps: PriceSeries, period: int = 20):
    df = ps.candles
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': df['close'].ewm(span=period, adjust=False).mean()
    }).set_index('timestamp'), ps.timeframe)

def getRSI(ps: PriceSeries, period: int = 14):
    df = ps.candles
    #Ensure 'close' column is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': calcRSI(df['close'], period),
    }), ps.timeframe)

def getWRSI(ps: PriceSeries, period: int = 14):
    df = ps.candles
    #Ensure 'close' column is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': calcWRSI(df['close'], period).values,
    }), ps.timeframe)
