import pandas as pd
from .plot.plotting import Plotting
from .dataTypes import Position
from .strategies import Strategy



class TestTrader:

    def __init__( 
            self,
            df: pd.DataFrame,
            initial_margin: float
        ):
        self.df = df
        self.initial_margin = initial_margin
        self.open_positions: list[Position] = []

    def open_position(self, new_position: Position):
        self.open_positions.append(new_position)
        return self.open_positions[-1]

    def close_position(self, p_timeframe):
        return next((pos for pos in self.open_positions if pos.open_timeframe == p_timeframe), None)
    
    def operate_strategy(self, ind, strategy: Strategy, plot: Plotting):
        for i in range(len(self.df)):
            resp = strategy.check_condition(ind[0:i])
            if(resp.count('OPEN_LONG')):
                pos = self.open_position(Position(
                    basicPosition, 
                    entry_price=self.df['Close'].iat[i],
                    open_timeframe=self.df.index[i]
                ))
                plot.plotPosition(pos)
            if(resp.count('CLOSE_LONG')):
                pos = self.open_position(Position(
                    basicPosition,
                    position_side='SHORT',
                    entry_price=self.df['Close'].iat[i],
                    open_timeframe=self.df.index[i]
                ))
                plot.plotPosition(pos)


basicPosition = {
    'symbol': 'btcusdt',
    'is_open': True,
    'type': 'Spot',
    'position_side': 'LONG',
    'position_size': 1,
}   

        
