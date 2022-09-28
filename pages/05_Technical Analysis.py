# web development
import streamlit as st
# Data Handling
import pandas as pd
import numpy as np
# Date time format
import datetime as dt
# Technical indicators
from finta import TA
# Financial information
import yfinance as yf 
# Read in API as a df format
import pandas_datareader.data as web

import mplfinance as mpf
import hvplot.pandas

#Candlestick Chart
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dow = 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW'

sp500 = 'MMM', 'AOS', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADM', 'ADBE', 'AAP', 'AMD', 'AES', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BBWI', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF.B', 'CHRW', 'CDNS', 'CZR', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CDAY', 'CERN', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CPRT'  'GLW', 'CTVA', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'LLY', 'EMR', 'ENPH', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'RE', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FRC', 'FE', 'FISV', 'FLT', 'FMC', 'F', 'FTNT', 'FTV',  'FBHS', 'FOXA', 'FOX', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GS', 'HAL', 'HBI', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'INFO', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT', 'JKHY', 'J', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU',  'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', 'LEN', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC', 'NLOK', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'OGN', 'OTIS', 'PCAR', 'PKG', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PBCT', 'PEP', 'PKI', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PTC', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'QCOM', 'PWR', 'DGX', 'RL', 'RJF',  'RTX', 'O', 'REG', 'REGN', 'RF',  'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'COO', 'HIG', 'HSY', 'MOS', 'TRV', 'DIS', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRMB', 'TFC', 'TWTR', 'TYL', 'TSN', 'USB', 'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VIAC', 'VTRS', 'V', 'VNO', 'VMC', 'WRB', 'GWW', 'WAB', 'WBA', 'WMT', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XLNX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS'

tickers = (dow + sp500)

tickers_dropdown = st.selectbox('Choose a stock ticker', tickers)

ohlc = web.DataReader(tickers_dropdown, 'yahoo') #, start='2019-09-10', end='2019-10-09')
ohlc = ohlc.rename(columns={'High':'high', 'Low':'low', 'Open':'open', 'Close':'close', 'Volume':'volume', 'Adj Close':'adj close'})
ohlc = ohlc.sort_index(ascending=False)

moving_average_df = ohlc[['close']]
oscillator_df = ohlc[['close']]

###################################
# Matrix
##################################

# Call in the asset using the API
monthly = yf.Ticker(tickers_dropdown).history(interval='1mo', period="max")
monthly = monthly[['Open', 'High', 'Low', 'Close']].sort_index(ascending=False).dropna()

weekly = yf.Ticker(tickers_dropdown).history(interval='1wk', period="max")
weekly = weekly[['Open', 'High', 'Low', 'Close']].sort_index(ascending=False).dropna()

daily = yf.Ticker(tickers_dropdown).history(interval='1d', period="5y")
daily = daily[['Open', 'High', 'Low', 'Close']].sort_index(ascending=False).dropna()

hourly = yf.Ticker(tickers_dropdown).history(interval='60m')
hourly = hourly[['Open', 'High', 'Low', 'Close']].sort_index(ascending=False).dropna()


# specify the subplot grid
fig = make_subplots(rows=2, cols=2, subplot_titles=("Monthly Timeframe", "Weekly Timeframe", "Daily Timeframe", "Hourly Timeframe"), shared_xaxes=False)

# Speciy the traces in the grid

fig.add_trace(go.Candlestick(
    x=monthly.index,
    open = monthly['Open'].tail(120),
    high = monthly['High'].tail(120),
    low = monthly['Low'].tail(120),
    close = monthly['Close'].tail(120),
    name = "Monthly Timeframe"),
              row=1, col=1)

fig.add_trace(go.Candlestick(
    x=weekly.index,
    open = weekly['Open'].tail(120),
    high = weekly['High'].tail(120),
    low = weekly['Low'].tail(120),
    close = weekly['Close'].tail(120),
    name = "Weekly Timeframe"),
              row=1, col=2)

fig.add_trace(go.Candlestick(
    x=daily.index,
    open = daily['Open'].tail(120),
    high = daily['High'].tail(120),
    low = daily['Low'].tail(120),
    close = daily['Close'].tail(120),
    name = "Daily Timeframe"),
              row=2, col=1)

fig.add_trace(go.Candlestick(
    x=hourly.index,
    open = hourly['Open'].tail(120),
    high = hourly['High'].tail(120),
    low = hourly['Low'].tail(120),
    close = hourly['Close'].tail(120),
    name = "Hourly Timeframe"),
              row=2, col=2)

# Update subplot grid with parameters
fig.update_layout(height=750, width=1050, showlegend=False)
fig.update_xaxes(rangeslider_visible=False)



##############################################
# st.dataframe(ohlc)

st.plotly_chart(fig, use_container_width=True)
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
    
