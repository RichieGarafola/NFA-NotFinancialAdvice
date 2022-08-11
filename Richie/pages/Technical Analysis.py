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

##############################################
# st.dataframe(ohlc)

st.set_option('deprecation.showPyplotGlobalUse', False)
initial_ohlc = mpf.plot(ohlc.tail(120), type = 'candle', style = 'yahoo')
st.pyplot(initial_ohlc)
###############################################

moving_average_dictionary = { 'SMA':'SimpleMovingAverage', 'SMM':'SimpleMovingMedian', 'SSMA':'SmoothedSimpleMovingAverage', 'EMA':'ExponentialMovingAverage', 'DEMA':'DoubleExponentialMovingAverage', 'TEMA':'TripleExponentialMovingAverage', 'TRIMA':'TriangularMovingAverage', 'VAMA':'VolumeAdjustedMovingAverage', 'KAMA':'KaufmansAdaptiveMovingAverage', 'ZLEMA':'ZeroLagExponentialMovingAverage', 'WMA':'WeightedMovingAverage', 'HMA':'HullMovingAverage', 'EVWMA':'ElasticVolumeMovingAverage', 'SMMA':'SmoothedMovingAverage', 'FRAMA':'FractalAdaptiveMovingAverage'}

    
oscillator_dictionary = {'TRIX':'TripleExponentialMovingAverageOscillator', 'ER':'KaufmanEfficiencyIndicator', 'PPO':'PercentagePriceOscillator', 'STOCH':'StochasticOscillator%K', 'STOCHD':'Stochasticoscillator%D', 'STOCHRSI':'StochasticRSI', 'UO':'UltimateOscillator', 'AO':'AwesomeOscillator', 'CHAIKIN':'ChaikinOscillator', 'VZO':'VolumeZoneOscillator', 'PZO':'PriceZoneOscillator', 'CMO':'ChandeMomentumOscillator', 'WTO':'WaveTrendOscillator'}

technical_analysis_dictionary = { 'SMA':'SimpleMovingAverage', 'SMM':'SimpleMovingMedian', 'SSMA':'SmoothedSimpleMovingAverage', 'EMA':'ExponentialMovingAverage', 'DEMA':'DoubleExponentialMovingAverage', 'TEMA':'TripleExponentialMovingAverage', 'TRIMA':'TriangularMovingAverage', 'TRIX':'TripleExponentialMovingAverageOscillator', 'VAMA':'VolumeAdjustedMovingAverage', 'ER':'KaufmanEfficiencyIndicator', 'KAMA':'KaufmansAdaptiveMovingAverage', 'ZLEMA':'ZeroLagExponentialMovingAverage', 'WMA':'WeightedMovingAverage', 'HMA':'HullMovingAverage', 'EVWMA':'ElasticVolumeMovingAverage', 'VWAP':'VolumeWeightedAveragePrice', 'SMMA':'SmoothedMovingAverage', 'FRAMA':'FractalAdaptiveMovingAverage', 'MACD':'MovingAverageConvergenceDivergence', 'PPO':'PercentagePriceOscillator', 'VW_MACD':'Volume-WeightedMACD', 'EV_MACD':'Elastic-VolumeweightedMACD', 'MOM':'MarketMomentum', 'ROC':'Rate-of-Change', 'RSI':'RelativeStrenghtIndex', 'IFT_RSI':'InverseFisherTransformRSI', 'TR':'TrueRange', 'ATR':'AverageTrueRange', 'SAR':'Stop-and-Reverse', 'BBANDS':'BollingerBands', 'BBWIDTH':'BollingerBandsWidth', 'MOBO':'MomentumBreakoutBands', 'PERCENT_B':'PercentB', 'KC':'KeltnerChannels', 'DO':'DonchianChannel', 'DMI':'DirectionalMovementIndicator', 'ADX':'AverageDirectionalIndex', 'PIVOT':'PivotPoints', 'PIVOT_FIB':'FibonacciPivotPoints', 'STOCH':'StochasticOscillator%K', 'STOCHD':'Stochasticoscillator%D', 'STOCHRSI':'StochasticRSI', 'WILLIAMS':'Williams%R', 'UO':'UltimateOscillator', 'AO':'AwesomeOscillator', 'MI':'MassIndex', 'VORTEX':'VortexIndicator', 'KST':'KnowSureThing', 'TSI':'TrueStrengthIndex', 'TP':'TypicalPrice', 'ADL':'Accumulation-DistributionLine', 'CHAIKIN':'ChaikinOscillator', 'MFI':'MoneyFlowIndex', 'OBV':'OnBalanceVolume', 'WOBV':'WeighterOBV', 'VZO':'VolumeZoneOscillator', 'PZO':'PriceZoneOscillator', 'EFI':'EldersForceIndex', 'CFI':'CummulativeForceIndex', 'EBBP':'BullpowerandBearPower', 'EMV':'EaseofMovement', 'CCI':'CommodityChannelIndex', 'COPP':'CoppockCurve', 'BASP':'BuyandSellPressure', 'BASPN':'NormalizedBASP', 'CMO':'ChandeMomentumOscillator', 'CHANDELIER':'ChandelierExit', 'QSTICK':'Qstick', 'TMF':'TwiggsMoneyIndex', 'WTO':'WaveTrendOscillator', 'FISH':'FisherTransform', 'ICHIMOKU':'IchimokuCloud', 'APZ':'AdaptivePriceZone', 'SQZMI':'SqueezeMomentumIndicator', 'VPT':'VolumePriceTrend', 'FVE':'FiniteVolumeElement', 'VFI':'VolumeFlowIndicator', 'MSD':'MovingStandarddeviation', 'STC':'SchaffTrendCycle', }


###################################
# Moving Averages
###################################


# ma = st.number_input(
#     'Moving Average Length',
#     value = 20,
#     min_value = 1,
#     max_value = 500,
#     step = 1,)

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
    # row = 1,
    # col = 1,
    )
    

# indicator 
fig.add_trace(
    go.Scatter(
        x=ohlc.index, 
        y=ohlc[f'{choice_of_moving_average}'], 
        marker_color='tomato',
        name=f'{choice_of_moving_average}'
    ),
    row = 1,
    col = 1,    
)

st.plotly_chart(fig)


###############################################
# oscillators
###############################################

# Selectbox of indicators that can be picked
choice_of_oscillators = st.selectbox('Choose an oscillators indicator', oscillator_dictionary,) # ma)
oscillators_indicator = getattr(TA,choice_of_oscillators)

# create dataframe for the indicator to be studied
oscillators_indicator_df = pd.DataFrame(oscillators_indicator(ohlc))

# Add indicator_df to the ohlc dataframe
ohlc[[f'{choice_of_oscillators}']] = oscillators_indicator_df


# Create a line plot to visualize
line_plot = ohlc[["close", f"{choice_of_oscillators}"]].hvplot(
    title=f'{choice_of_oscillators}',
    ylabel="Price",
    xlabel="Date",
    width=1000,
    height=400
)
st.pyplot(line_plot)


# fig = make_subplots(
#     rows = 2, 
#     cols = 1,
#     shared_xaxes = True,
#     vertical_spacing = 0.10,
#     subplot_titles = (f'{tickers_dropdown}', f'{choice_of_oscillators} oscillator' ),
#         row_width = [0.3, 0.7])

# fig.add_trace(
#     go.Candlestick(
#         x = ohlc.index,
#         open = ohlc['open'], 
#         high = ohlc['high'],
#         low = ohlc['low'],
#         close = ohlc['close'],
#         name = 'Candlestick chart'
#     ),
#     row = 1,
#     col = 1,
#     )
    
# # indicator 
# fig.add_trace(
#     go.Scatter(
#         x=ohlc.index, 
#         y=ohlc[f'{choice_of_oscillators}'], 
#         marker_color='tomato',
#         name=f'{choice_of_oscillators}'))

# st.plotly_chart(fig)

