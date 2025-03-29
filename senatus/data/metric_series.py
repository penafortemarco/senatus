import pandas as pd

class MetricSeries:

    def __init__(
        self,
        data_frame: pd.DataFrame,
        timeframe: str,
    ):  
        self.series = data_frame
        self.timeframe = timeframe
        self.series['timestamp'] = pd.to_datetime(self.series['timestamp'])
        self.series.set_index('timestamp', inplace=True)

    