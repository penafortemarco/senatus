from senatus.api.binanceAPI import (getPastCandlesTimeSeries)
from senatus.indicators.indicators import (getMAV, getEMA, getWRSI, find_top)
from senatus.plot import Plot
from senatus.test_trader import TestTrader
from senatus.strategies import RSI_Margins_Strategy, BoolIndicatorStrategy

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

is_top = find_top(priceSeries, 25, 0)

tt = TestTrader(priceSeries, 1000)

#tt.operate_strategy(is_top, BoolIndicatorStrategy(), my_plot)

#tt.operate_strategy(wrsi, RSI_Margins_Strategy(15, 80), my_plot)

my_plot.apply_custom().show()