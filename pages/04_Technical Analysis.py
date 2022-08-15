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



tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
tickers_dropdown = st.selectbox('Choose a stock ticker', tickers)

ohlc = web.DataReader(tickers_dropdown, 'yahoo') #, start='2019-09-10', end='2019-10-09')
ohlc = ohlc.rename(columns={'High':'high', 'Low':'low', 'Open':'open', 'Close':'close', 'Volume':'volume', 'Adj Close':'adj close'})


ohlc = ohlc.sort_index(ascending=False)


moving_average_df = ohlc[['close']]
oscillator_df = ohlc[['close']]

##############################################
# st.dataframe(ohlc)

st.set_option('deprecation.showPyplotGlobalUse', False)
initial_ohlc = mpf.plot(ohlc.tail(120), type = 'candle', style = 'yahoo')

col1, col2 = st.columns([3, 1])

col1.subheader(f"{tickers_dropdown} Daily Candlestick Chart")
col1.pyplot(initial_ohlc)

col2.subheader(f"{tickers_dropdown} data")
col2.write(ohlc)
###############################################

moving_average_dictionary = { 'SMA':'SimpleMovingAverage', 'SMM':'SimpleMovingMedian', 'SSMA':'SmoothedSimpleMovingAverage', 'EMA':'ExponentialMovingAverage', 'DEMA':'DoubleExponentialMovingAverage', 'TEMA':'TripleExponentialMovingAverage', 'TRIMA':'TriangularMovingAverage', 'VAMA':'VolumeAdjustedMovingAverage', 'KAMA':'KaufmansAdaptiveMovingAverage', 'ZLEMA':'ZeroLagExponentialMovingAverage', 'WMA':'WeightedMovingAverage', 'HMA':'HullMovingAverage', 'EVWMA':'ElasticVolumeMovingAverage', 'SMMA':'SmoothedMovingAverage', 'FRAMA':'FractalAdaptiveMovingAverage'}

# Selectbox of indicators that can be picked
choice_of_moving_average = st.sidebar.selectbox('Choose a Moving Average indicator', moving_average_dictionary,)

oscillator_dictionary = {'STOCHRSI':'StochasticRSI', 'AO':'AwesomeOscillator', 'CHAIKIN':'ChaikinOscillator', 'VZO':'VolumeZoneOscillator', 'PZO':'PriceZoneOscillator', 'CMO':'ChandeMomentumOscillator'}

# Selectbox of oscillators that can be picked
choice_of_oscillator = st.sidebar.selectbox('Choose an oscillator', oscillator_dictionary,)

###################################
# Moving Averages
###################################


x = st.sidebar.number_input("how many days Moving Average?", min_value=3)

moving_average_df['SMA'] = TA.SMA(ohlc, x)
moving_average_df['SMM'] = TA.SMM(ohlc, x)
moving_average_df['SSMA'] = TA.SSMA(ohlc, x)
moving_average_df['EMA'] = TA.EMA(ohlc, x)
moving_average_df['TEMA'] = TA.TEMA(ohlc, x)
moving_average_df['TRIMA'] = TA.TRIMA(ohlc, x)
moving_average_df['VAMA'] = TA.VAMA(ohlc, x)
moving_average_df['KAMA'] = TA.KAMA(ohlc, x)
moving_average_df['ZLEMA'] = TA.ZLEMA(ohlc, x)
moving_average_df['WMA'] = TA.WMA(ohlc, x)
moving_average_df['HMA'] = TA.HMA(ohlc, x)
moving_average_df['EVWMA'] = TA.EVWMA(ohlc, x)
moving_average_df['SMMA'] = TA.SMMA(ohlc, x)

# indicator 
moving_average_fig = go.Figure()

moving_average_fig.add_trace(
    go.Candlestick(
        x = ohlc.index,
        open = ohlc['open'], 
        high = ohlc['high'],
        low = ohlc['low'],
        close = ohlc['close'],
        name = 'Candlestick chart'
    ))
moving_average_fig.add_trace(
    go.Scatter(
        x=moving_average_df.index, 
        y=moving_average_df[f'{choice_of_moving_average}'], 
        marker_color='tomato',
        name=f'{choice_of_moving_average}'))

# st.plotly_chart(moving_average_fig)


###################################
# Oscillators
###################################


oscillator_df['STOCHRSI'] = TA.STOCHRSI(ohlc, x)
oscillator_df['AO'] = TA.AO(ohlc, x)
oscillator_df['CHAIKIN'] = TA.CHAIKIN(ohlc, x)
oscillator_df['VZO'] = TA.VZO(ohlc, x)
oscillator_df['PZO'] = TA.PZO(ohlc, x)
oscillator_df['CMO'] = TA.CMO(ohlc, x)

# indicator 
oscillator_fig = go.Figure()
oscillator_fig.add_trace(
    go.Scatter(
        x=oscillator_df.index, 
        y=oscillator_df[f'{choice_of_oscillator}'], 
        marker_color='tomato',
        name=f'{choice_of_oscillator}'))

# st.plotly_chart(oscillator_fig)

col1, col2 = st.columns(2)

with col1:
    st.header("Moving Averages")
    st.plotly_chart(moving_average_fig)

with col2:
    st.header("Oscillator")
    st.plotly_chart(oscillator_fig)
