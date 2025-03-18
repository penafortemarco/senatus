import numpy as np
import pandas as pd
from .calc_metrics import (calcRSI, calcWRSI)

def getMAV(df: pd.DataFrame, period: int = 20):
    return pd.DataFrame({
        'Date': df.index,
        'Value': df['Close'].rolling(window=period).mean()
    }).set_index('Date')

def getEMA(df: pd.DataFrame, period: int = 20):
    return pd.DataFrame({
        'Date': df.index,
        'Value': df['Close'].ewm(span=period, adjust=False).mean()
    }).set_index('Date')

def getRSI(df: pd.DataFrame, period: int = 14):
    #Ensure 'Close' column is numeric
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Value'] = calcRSI(df['Close'], period)
    return df[['Value']]

def getWRSI(df: pd.DataFrame, period: int = 14):
    #Ensure 'Close' column is numeric
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Value'] = calcWRSI(df['Close'], period).values
    return df[['Value']]