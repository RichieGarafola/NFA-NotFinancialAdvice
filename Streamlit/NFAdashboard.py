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

############################################

# Pick your Tickers / Display Cumulative Returns of Tickers

############################################

# Tickers from the Dow 30 from YFinance
tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')

# Takes the tickers and puts them in a list to be Multi selected in a dropdown
dropdown = st.multiselect('Pick your assets', tickers)

# Start time
start = st.date_input('Start', value = pd.to_datetime('2020-01-01'))

# Relative return of the users deseired stock.
def relativereturn(df):
    rel = df.pct_change()
    cumulativereturn = (1-rel).cumprod() -1
    cumulativereturn = cumulativereturn.fillna(0)
    return cumulativereturn

# Starts the drop down at 0 to remove an initial error 
if len(dropdown) > 0:
#     df = yf.download(dropdown,start,end)['Adj Close']
    df = relativereturn(yf.download(dropdown,start)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    
############################################

# Company Information

############################################

# Use the Pathlib libary to set the path to the CSV
csv_path = Path('Desktop/project 3/Project3/Richie/Streamlit/Resources/fundamental_info_df.csv')

# Use the file path to read the CSV into a DataFrame
fundamental_info_df = pd.read_csv(csv_path, index_col = 'symbol')

# list of all available information for the yfinance dictionary in dataframe format
list = fundamental_info_df[['longBusinessSummary', 'previousClose', 'open', 'bid', 'ask', 'dayHigh', 'dayLow', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', '52WeekChange', 'volume', 'averageVolume', 'marketCap', 'beta', 'earningsGrowth', 'dividendYield']]

# Cherry picked list of useful information keys in list format
list_of_lists = ['previousClose', 'open', 'bid', 'ask', 'dayHigh', 'dayLow', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', '52WeekChange', 'volume', 'averageVolume', 'marketCap', 'beta', 'earningsGrowth', 'dividendYield']

list_of_all_company_information = ('zip', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 
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

st.title("Information on the company")

# Individual, selectbox
dropdown2 = st.selectbox('What company are you interested in?', tickers)

# Create a dropdown of all availabile information on the company the user selects. 
company_information_dropdown = st.selectbox('What information on the company are you interested in?', list_of_all_company_information)

# make an API call based on the ticker the user selected using the information selected from 'list_of_all_company_information' dropdown
information = yf.Ticker(dropdown2).info[f"{company_information_dropdown}"]

# Display information
st.write(information)

# This piece uses the csv file to expedite load time.

dropdown3 = st.selectbox('What would you like to look at more close?', list_of_lists)
# Display the top 10s and the barchart side by side using the column function
col1, col2 = st.columns(2)
with col1:
    st.table(list[f'{dropdown3}'].nlargest(10))
with col2:
    st.bar_chart(list[f'{dropdown3}'])

        
############################################

# Fundamental Analysis

############################################

analysis_list = ('info', 'actions', 'dividends', 'splits', 'financials', 'quarterly_financials', 'major_holders', 'institutional_holders', 'quarterly_balance_sheet', 'cashflow', 'quarterly_cashflow', 'earnings', 'quarterly_earnings', 'sustainability', 'recommendations', 'calendar', 'earnings_dates', 'options', 'news') 

analysis_dropdown = st.selectbox('What fundamental analysis are you interested in?', analysis_list).strip("''")


# """
# @ TO DO : Read in the fundamental analysis from the api.

# problem with current code:
# output from the selectbox gives us quotes around the output.

# the way the function works is:

#         # Example for show analysts recommendations
#         msft.recommendations
#         in our case:
#         dropdown2.analysis_dropdown

# """
#########################

# analysis = yf.Ticker(dropdown2).info[f'{analysis_dropdown}']

analysis_dropdown = analysis_dropdown.strip("''")
#st.write(f"dropdown2.{analysis_dropdown}")
st.table(getattr(yf.Ticker(dropdown2),analysis_dropdown))
#yf.Ticker(analysis_dropdown)