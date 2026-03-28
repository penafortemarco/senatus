# Senatus

[![PyPI version](https://img.shields.io/pypi/v/senatus)](https://pypi.org/project/senatus/)
[![Python](https://img.shields.io/pypi/pyversions/senatus)](https://pypi.org/project/senatus/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)

A WIP Python library for building trading bots and performing market analysis. Senatus wraps the Binance API (spot and futures) and provides utilities for retrieving market data, computing technical indicators, and visualizing results — so you can focus on strategy logic instead of boilerplate.

---

## Features

- **Binance integration** — spot and futures market data via `binance-connector` and `binance-futures-connector`
- **Data handling** — market data returned as `pandas` DataFrames, ready for analysis
- **Numerical analysis** — `numpy`-based computations for signal processing and indicator math
- **Visualization** — interactive charts via `plotly` for exploring price action and indicators
- **(WIP)Bot-ready** — designed as a foundation for automated trading strategies

---

## Installation

```bash
pip install senatus
```

### Virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install senatus
```

---

## Quickstart

```python
# Example: fetch OHLCV data and compute a simple moving average
# (full API reference coming soon — see the senatus/ source directory)

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

# Test bot
tt.operate_strategy(is_top, BoolIndicatorStrategy(), my_plot)
tt.operate_strategy(wrsi, RSI_Margins_Strategy(15, 80), my_plot)

my_plot.apply_custom().show()
```

> Full quickstart examples are in progress. See the `senatus/` package directory for available modules and the `test/` directory for usage patterns.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `numpy >= 2.2.3` | Numerical computation |
| `pandas >= 2.2.3` | Market data as DataFrames |
| `plotly >= 5.24.0` | Interactive charting |
| `binance-connector >= 3.12.0` | Binance Spot API |
| `binance-futures-connector >= 4.1.0` | Binance Futures API |

---

## Project Structure

```
senatus/
├── senatus/        # Core library package
├── test/           # Tests and usage examples
├── pyproject.toml  # Package metadata and dependencies
└── LICENSE.txt
```

---

## Roadmap

- [X] Initial technical indicator library (RSI, MACD, Bollinger Bands, etc.)
- [ ] Complete quickstart documentation with code examples
- [ ] Backtesting utilities
- [ ] Strategy base class for building trading bots

---

## License

MIT — see [LICENSE.txt](LICENSE.txt) for details.

---

## Author

**Marco Penaforte** — [LinkedIn](https://linkedin.com/in/penafortemarco) · [Portfolio](https://marcopenaforte.space)
