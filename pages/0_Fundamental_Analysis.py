# web development
import streamlit as st
# Data Handling
import pandas as pd
# Date time format
import datetime as dt
# Visualize Results
import matplotlib.pyplot as plt
# Pull in financial information
import yfinance as yf

from pathlib import Path

# Configure Streamlit page settings
st.set_page_config(
    page_title="NFA Dash",
    page_icon="📊",
    layout="wide"
)

# dashboard title
st.title("NotFinancialAdvice")

############################################

# Pick your Tickers / Display Cumulative Returns of Tickers

############################################

# Tickers from the Dow 30 from YFinance
dow = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')

# Tickers from the sp500 from YFinance
sp500 = ('MMM', 'AOS', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADM', 'ADBE', 'AAP', 'AMD', 'AES', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BBWI', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF.B', 'CHRW', 'CDNS', 'CZR', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CDAY', 'CERN', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CPRT'  'GLW', 'CTVA', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'LLY', 'EMR', 'ENPH', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'RE', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FRC', 'FE', 'FISV', 'FLT', 'FMC', 'F', 'FTNT', 'FTV',  'FBHS', 'FOXA', 'FOX', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GS', 'HAL', 'HBI', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'INFO', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT', 'JKHY', 'J', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU',  'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', 'LEN', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC', 'NLOK', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'OGN', 'OTIS', 'PCAR', 'PKG', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PBCT', 'PEP', 'PKI', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PTC', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'QCOM', 'PWR', 'DGX', 'RL', 'RJF',  'RTX', 'O', 'REG', 'REGN', 'RF',  'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'COO', 'HIG', 'HSY', 'MOS', 'TRV', 'DIS', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRMB', 'TFC', 'TWTR', 'TYL', 'TSN', 'USB', 'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VIAC', 'VTRS', 'V', 'VNO', 'VMC', 'WRB', 'GWW', 'WAB', 'WBA', 'WMT', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XLNX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS')

tickers = dow + sp500

st.title("Information on the company")

# Pick your Tickers / Display Cumulative Returns of Tickers
# Takes the tickers and puts them in a list to be Multi selected in a dropdown
dropdown = st.multiselect('Pick your assets', tickers)

# Start time
start = st.date_input('Start', value=pd.to_datetime('2020-01-01'))

# Relative return of the users deseired stock.
@st.cache
def relative_return(df):
    """
    Calculates the relative returns by taking 
    the percentage change and cumulatively 
    multiplying the changes
    """
    rel = df.pct_change().cumprod() - 1
    return rel.fillna(0)

# Start the drop down at 0 to remove an initial error 
if len(dropdown) > 0:
    # Download the closing price data for the selected tickers 
    # from Yahoo Finance starting from the specified date
    df = yf.download(dropdown, start)['Close']
    st.header('Closing price of {}'.format(dropdown))
    # Display the closing price data as a line chart  
    st.line_chart(df)
    
############################################

# Company Information

############################################

# Use the Pathlib libary to set the path to the CSV
csv_path = Path('Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/fundamental_info_df.csv')

# Read the CSV file containing fundamental information about the companies and set the index column to 'symbol'
fundamental_info_df = pd.read_csv(csv_path, index_col='symbol')

# Cherry picked list of useful information keys in list format
list_of_lists = [
    'previousClose', 'open', 'bid', 'ask', 'dayHigh', 'dayLow', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', '52WeekChange',
    'volume', 'averageVolume', 'marketCap', 'beta', 'earningsGrowth', 'dividendYield'
]

# Select the company of interest from the dropdown menu
dropdown2 = st.selectbox('What company are you interested in?', tickers)

# Select the specific information about the company to display from the fundamental_info_df
company_information_dropdown = st.selectbox('What information on the company are you interested in?', fundamental_info_df.columns)

# Retrieve information about the selected company from Yahoo Finance using the Ticker object
ticker = yf.Ticker(dropdown2)
try:
    
     # Retrieve the selected company information from the ticker object and displays it
    information = ticker.info.get(company_information_dropdown)
    st.write(information)
except:
    # Display an error message if failed to retrieve the information
    st.write("Error: Failed to retrieve information. Please check the ticker symbol or try again later.")

# Use the csv file to expedite load time.
# Create side by side columns of the top 10 companys and a barchart of all companies as a visual based on the users selection.
dropdown3 = st.selectbox('What would you like to look at more closely?', list_of_lists)

# Use the column function
col1, col2 = st.columns([1,3])
with col1:
    # Display the top 10 values for the selected fundamental information in a table
    st.dataframe(fundamental_info_df[dropdown3].nlargest(10))
with col2:
    col2.subheader("Top Stock Comparison")
    # Display a bar chart comparing the selected fundamental information across different companies
    st.bar_chart(fundamental_info_df[dropdown3])

############################################

# Fundamental Analysis

############################################  

# List of all analysis offered
analysis_list = [
    'actions', 'dividends', 'splits', 'financials', 'quarterly_financials', 'major_holders',
    'institutional_holders', 'quarterly_balance_sheet', 'cashflow', 'quarterly_cashflow', 'earnings', 'quarterly_earnings', 'sustainability', 'recommendations', 'calendar', 'earnings_dates', 'options', 'news'
]

# Select the type of fundamental analysis to perform from the dropdown menu
analysis_dropdown = st.selectbox('What fundamental analysis are you interested in?', analysis_list).strip("''")

# Retrieve the fundamental analysis data for the selected company and analysis type and displays it as a table
try:
    analysis_data = getattr(yf.Ticker(dropdown2), analysis_dropdown)
    st.dataframe(analysis_data)
    # sorted_data = analysis_data.sort_values(ascending=False)
    # st.dataframe(sorted_data)
except:
    # Display an error message if failed to retrieve the fundamental analysis

    st.write("Error: Failed to retrieve fundamental analysis. Please choose another fundamental insight.")

# st.caption('Created by Richie Garafola, Mark Staten, Jacob Edelbrock 8/22')
# st.caption('Updated by Richie Garafola 5/23')