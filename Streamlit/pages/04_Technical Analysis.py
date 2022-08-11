import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from finta import TA
import yfinance as yf 
import pandas_datareader.data as web

import mplfinance as mpf
import hvplot.pandas

#Candlestick Chart
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tab1, tab2 = st.tabs(["Candlestick Chart", "Moving Averages"])


tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
tickers_dropdown = st.selectbox('Choose a stock ticker', tickers)

ohlc = web.DataReader(tickers_dropdown, 'yahoo') #, start='2019-09-10', end='2019-10-09')
ohlc = ohlc.rename(columns={'High':'high', 'Low':'low', 'Open':'open', 'Close':'close', 'Volume':'volume', 'Adj Close':'adj close'})


##############################################
# st.dataframe(ohlc)

st.set_option('deprecation.showPyplotGlobalUse', False)
initial_ohlc = mpf.plot(ohlc.tail(120), type = 'candle', style = 'yahoo')

col1, col2 = st.columns([3, 1])

col1.subheader(f"{tickers_dropdown} candlestick chart")
col1.pyplot(initial_ohlc)

col2.subheader(f"{tickers_dropdown} data")
col2.write(ohlc)
###############################################

moving_average_dictionary = { 'SMA':'SimpleMovingAverage', 'SMM':'SimpleMovingMedian', 'SSMA':'SmoothedSimpleMovingAverage', 'EMA':'ExponentialMovingAverage', 'DEMA':'DoubleExponentialMovingAverage', 'TEMA':'TripleExponentialMovingAverage', 'TRIMA':'TriangularMovingAverage', 'VAMA':'VolumeAdjustedMovingAverage', 'KAMA':'KaufmansAdaptiveMovingAverage', 'ZLEMA':'ZeroLagExponentialMovingAverage', 'WMA':'WeightedMovingAverage', 'HMA':'HullMovingAverage', 'EVWMA':'ElasticVolumeMovingAverage', 'SMMA':'SmoothedMovingAverage', 'FRAMA':'FractalAdaptiveMovingAverage'}

    
###################################
# Moving Averages
###################################

# Selectbox of indicators that can be picked
choice_of_moving_average = st.selectbox('Choose a Moving Average indicator', moving_average_dictionary,) # ma)
moving_average_indicator = getattr(TA,choice_of_moving_average)

# create dataframe for the indicator to be studied
moving_average_indicator_df = pd.DataFrame(moving_average_indicator(ohlc))

# Add indicator_df to the ohlc dataframe
ohlc[[f'{choice_of_moving_average}']] = moving_average_indicator_df

fig = make_subplots(
    rows = 2, 
    cols = 1,
    shared_xaxes = True,
    vertical_spacing = 0.10,
    subplot_titles = (f'{tickers_dropdown}', f'{choice_of_moving_average} Moving Averages' ),
        row_width = [0.3, 0.7]
    )

fig.add_trace(
    go.Candlestick(
        x = ohlc.index,
        open = ohlc['open'], 
        high = ohlc['high'],
        low = ohlc['low'],
        close = ohlc['close'],
        name = 'Candlestick chart'
    ),
    )
    

# indicator 
fig.add_trace(
    go.Scatter(
        x=ohlc.index, 
        y=ohlc[f'{choice_of_moving_average}'], 
        marker_color='tomato',
        name=f'{choice_of_moving_average}'
    ),
)

st.plotly_chart(fig)
