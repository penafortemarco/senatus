from senatus.binanceAPI import (getPastCandlesDF)
from senatus.indicators import (getMAV, getEMA, getWRSI)
from senatus.plot.plotting import Plotting
from senatus.trader import TestTrader
from senatus.strategies import RSI_Margins_Strategy

#Params
pair = 'bnbusdt'
timeframe = '1h'

#Get past data
pastDataFrame = getPastCandlesDF(pair, timeframe)

#Subscribe to stream data

#Plot data
my_plot = Plotting(pastDataFrame)

my_plot.plot_asset_chart()

wrsi = getWRSI(pastDataFrame, 8)

my_plot.plot_indicator_dif_chart(wrsi)


tt = TestTrader(pastDataFrame, 1000)
tt.operate_strategy(wrsi, RSI_Margins_Strategy(15, 80), my_plot)

my_plot.apply_custom().show()