import pandas as pd
from ..data import PriceSeries, MetricSeries
from .indicators_utils import (
    calcRSI, 
    calcWRSI,
    eval_top,
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
    # Ensure 'close' column is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': calcRSI(df['close'], period),
    }), ps.timeframe)

def getWRSI(ps: PriceSeries, period: int = 14):
    df = ps.candles
    # Ensure 'close' column is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': calcWRSI(df['close'], period).values,
    }), ps.timeframe)

def find_top(ps: PriceSeries, window: int = 5, middle_shift: int = 0):
    '''
    Useful to get Short signals at tops
    '''
    df = ps.candles
    # Ensure 'close' column is numeric
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return MetricSeries(pd.DataFrame({
        'timestamp': df.index,
        'value': eval_top(ps.candles['close'], window, middle_shift),
    }), ps.timeframe)