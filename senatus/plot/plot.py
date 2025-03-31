import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ..data import (PriceSeries, MetricSeries, Position)
from ..custom import stdLayout


class Plot():
    """
    A single plot, meant to represent an asset with info, data and analysis methods.
    Every instance methods return the instance itself (exept .show() which is supposed to run last), 
    allowing chain calling
    """

    def __init__(self,
            priceSeries: PriceSeries,
            main_figure_rows: int = 3,
            main_figure_cols: int = 1
        ):

        self.priceSeries = priceSeries
        self.main_figure = make_subplots(
            rows=main_figure_rows, 
            cols=main_figure_cols, 
            shared_xaxes=True, 
            vertical_spacing=0,
            specs=[[{"rowspan": 2}], [None], [{}]]
        )

    def plot_asset_chart(self):
        self.main_figure.add_trace( 
            go.Candlestick(
                x=self.priceSeries.candles.index,
                open=self.priceSeries.candles['open'],
                high=self.priceSeries.candles['high'],
                low=self.priceSeries.candles['low'],
                close=self.priceSeries.candles['close']
            ),
        )
        return self

    def apply_custom(self, layout = stdLayout):
        self.main_figure.update(layout_xaxis_rangeslider_visible=False)
        self.main_figure.update_layout(layout)
        return self

    def show(self):
        self.main_figure.show()

    def plot_indicator_same_chart(self, ind: MetricSeries):
        self.main_figure.add_trace(
            go.Scatter(
                x=ind.series.index,
                y=ind.series['value']
            )  
        )
        return self
    
    def plot_indicator_dif_chart(self, ind: MetricSeries, row=3, col=1):
        self.main_figure.add_trace(
            go.Scatter(
                x=ind.series.index, y=ind.series['value']
            ),
            row=row,
            col=col
        )
        return self

    def plotPosition(self, pos: Position):
        if(pos.is_open):
            self.main_figure.add_trace(
                go.Scatter(
                    x=[pos.open_timeframe], 
                    y=[pos.entry_price], 
                    mode='markers',
                    marker=dict(size=[10], color=('green' if pos.position_side == 'LONG' else 'red'))),
                row=1,
                col=1
            )
        return self

    