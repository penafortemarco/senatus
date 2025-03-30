from senatus.api.binanceAPI import (getPastCandlesTimeSeries)
from senatus.indicators.indicators import (getMAV, getEMA, getWRSI, findTop )
from senatus.indicators import Plot
from senatus.trader import TestTrader
from senatus.strategies import RSI_Margins_Strategy

# Define your parameters
pair = 'bnbusdt'
timeframe = '1h'


# Get past data
priceSeries = getPastCandlesTimeSeries(pair, timeframe)


# Plot data
my_plot = Plot(priceSeries)

my_plot.plot_asset_chart()

wrsi = getWRSI(priceSeries, 8)

my_plot.plot_indicator_dif_chart(wrsi)

print()

tt = TestTrader(priceSeries, 1000)
tt.operate_strategy(wrsi, RSI_Margins_Strategy(15, 80), my_plot)

my_plot.apply_custom().show()