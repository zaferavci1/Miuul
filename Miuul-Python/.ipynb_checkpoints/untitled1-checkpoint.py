import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import yfinance as yf
from yahoofinancials import YahooFinancials
import plotly.graph_objects as go




apple_df = yf.download('AAPL',
                       start='2017-01-01',
                       progress=False)

apple_df.index = pd.to_datetime(apple_df.index)
print(apple_df)

fig = go.Figure(data=[go.Candlestick(x=apple_df.index,
                                     open = apple_df['Open'],
                                     high = apple_df['High'],
                                     low = apple_df['Low'],
                                     close = apple_df['Close'])])

fig.show()

