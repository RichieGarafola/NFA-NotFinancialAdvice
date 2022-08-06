# web development
import streamlit as st 
# Data Handling
import pandas as pd
# Date time format
import datetime as dt
# Visualize Results
import matplotlib.pyplot as plt
plt.style.use('seaborn')
# Pull in financial information
import yfinance as yf 

from pathlib import Path


# dashboard title
st.title("NotFinanialAdvice Streamlit Finance Dashboard")

# Tickers from the Dow 30 from YFinance
tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')

# Takes the tickers ans puts them in a list to be selected in a dropdown
dropdown = st.multiselect('Pick your assets', tickers)

# Start time
start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
# End time
end = st.date_input('End', value = pd.to_datetime('today'))

# Relative return of the users deseired stock.
def relativereturn(df):
    rel = df.pct_change()
    cumulativereturn = (1-rel).cumprod() -1
    cumulativereturn = cumulativereturn.fillna(0)
    return cumulativereturn


# Starts the drop down at 0 to remove an initial error 
if len(dropdown) > 0:
#     df = yf.download(dropdown,start,end)['Adj Close']
    df = relativereturn(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    
fundamentals_list = ('zip', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 
                       'city', 'phone', 'state', 'country', 'companyOfficers', 
                       'website', 'maxAge', 'address1', 'fax', 'industry', 
                       'ebitdaMargins', 'profitMargins', 'grossMargins', 
                       'operatingCashflow', 'revenueGrowth', 'operatingMargins', 
                       'ebitda', 'targetLowPrice', 'recommendationKey', 
                       'grossProfits', 'freeCashflow', 'targetMedianPrice', 
                       'currentPrice', 'earningsGrowth', 'currentRatio', 'returnOnAssets', 
                       'numberOfAnalystOpinions', 'targetMeanPrice', 'debtToEquity', 
                       'returnOnEquity', 'targetHighPrice', 'totalCash', 'totalDebt', 
                       'totalRevenue', 'totalCashPerShare', 'financialCurrency', 
                       'revenuePerShare', 'quickRatio', 'recommendationMean', 'exchange', 
                       'shortName', 'longName', 'exchangeTimezoneName', 
                       'exchangeTimezoneShortName', 'isEsgPopulated', 'gmtOffSetMilliseconds', 
                       'quoteType', 'symbol', 'messageBoardId', 'market', 'annualHoldingsTurnover', 
                       'enterpriseToRevenue', 'beta3Year', 'enterpriseToEbitda', '52WeekChange', 
                       'morningStarRiskRating', 'forwardEps', 'revenueQuarterlyGrowth', 
                       'sharesOutstanding', 'fundInceptionDate', 'annualReportExpenseRatio', 
                       'totalAssets', 'bookValue', 'sharesShort', 'sharesPercentSharesOut', 
                       'fundFamily', 'lastFiscalYearEnd', 'heldPercentInstitutions', 
                       'netIncomeToCommon', 'trailingEps', 'lastDividendValue', 
                       'SandP52WeekChange', 'priceToBook', 'heldPercentInsiders', 
                       'nextFiscalYearEnd', 'yield', 'mostRecentQuarter', 'shortRatio', 
                       'sharesShortPreviousMonthDate', 'floatShares', 'beta', 'enterpriseValue', 
                       'priceHint', 'threeYearAverageReturn', 'lastSplitDate', 'lastSplitFactor', 
                       'legalType', 'lastDividendDate', 'morningStarOverallRating', 
                       'earningsQuarterlyGrowth', 'priceToSalesTrailing12Months', 'dateShortInterest', 
                       'pegRatio', 'ytdReturn', 'forwardPE', 'lastCapGain', 'shortPercentOfFloat', 
                       'sharesShortPriorMonth', 'impliedSharesOutstanding', 'category', 
                       'fiveYearAverageReturn', 'previousClose', 'regularMarketOpen', 
                       'twoHundredDayAverage', 'trailingAnnualDividendYield', 'payoutRatio', 
                       'volume24Hr', 'regularMarketDayHigh', 'navPrice', 'averageDailyVolume10Day',  
                       
                       
                       'regularMarketPreviousClose', 'fiftyDayAverage', 'trailingAnnualDividendRate', 
                       'open', 'toCurrency', 'averageVolume10days', 'expireDate', 'algorithm', 
                       'dividendRate', 'exDividendDate', 'circulatingSupply', 'startDate', 
                       'regularMarketDayLow', 'currency', 'trailingPE', 'regularMarketVolume', 
                       'lastMarket', 'maxSupply', 'openInterest', 'marketCap', 'volumeAllCurrencies', 
                       'strikePrice', 'averageVolume', 'dayLow', 'ask', 'askSize', 'volume', 
                       'fiftyTwoWeekHigh', 'fromCurrency', 'fiveYearAvgDividendYield', 
                       'fiftyTwoWeekLow', 'bid', 'tradeable', 'dividendYield', 'bidSize', 'dayHigh',
                       'coinMarketCapLink', 'regularMarketPrice', 'preMarketPrice', 'logo_url', 
                       'trailingPegRatio')



# Use the Pathlib libary to set the path to the CSV
csv_path = Path("./Resources/fundamental_info_df.csv")

# Use the file path to read the CSV into a DataFrame and display a few rows
fundamental_info_df = pd.read_csv(csv_path, index_col = 'symbol')

matrix = fundamental_info_df[[fundamentals_list]]

st.write(matrix)

fundamental_dropdown = st.multiselect('Pick your fundamental interest', fundamentals_list)

st.write(dropdown.fundamental_list_df)