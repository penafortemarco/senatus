import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ..dataTypes import Position
from ..custom import myLayout


class Plotting():
    """
    A single plot
    This is meant to represent an asset with info, data, ploting and analysis methods
    Every instance methods return the instance itself (exept .show()), allowing chain calling
    """

    def __init__(self,
            ohlc_data_frame: pd.DataFrame = pd.DataFrame(),
            main_figure_rows: int = 3,
            main_figure_cols: int = 1
        ):

        self.ohlc_data_frame = ohlc_data_frame
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
                x=self.ohlc_data_frame.index,
                open=self.ohlc_data_frame['Open'],
                high=self.ohlc_data_frame['High'],
                low=self.ohlc_data_frame['Low'],
                close=self.ohlc_data_frame['Close']
            ),
        )
        return self

    def apply_custom(self, layout = myLayout):
        self.main_figure.update(layout_xaxis_rangeslider_visible=False)
        self.main_figure.update_layout(layout)
        return self

    def show(self):
        self.main_figure.show()

    def plot_indicator_same_chart(self, ind: pd.DataFrame):
        self.main_figure.add_trace(
            go.Scatter(
                x=ind.index,
                y=ind['Value']
            )  
        )
        return self
    
    def plot_indicator_dif_chart(self, ind: pd.DataFrame, row=3, col=1):
        self.main_figure.add_trace(
            go.Scatter(
                x=ind.index, y=ind['Value']
            ),
            row=row,
            col=col
        )
        return self

    def plotPosition(self, pos: Position):
        if(pos['is_open']):
            self.main_figure.add_trace(
                go.Scatter(
                    x=[pos['open_timeframe']], 
                    y=[pos['entry_price']], 
                    mode='markers',
                    marker=dict(size=[10], color=('green' if pos['position_side'] == 'LONG' else 'red'))),
                row=1,
                col=1
            )
        return self

    