import streamlit as st # web development
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="NotFinancialAdvice",
    page_icon="📊",
    layout= "wide"    
)

# dashboard title
st.title("NotFinanialAdvice Streamlit Finance Dashboard")

tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

def relativereturn(df):
    rel = df.pct_change()
    cumulativereturn = (1-rel).cumprod() -1
    cumulativereturn = cumulativereturn.fillna(0)
    return cumulativereturn



if len(dropdown) > 0:
#     df = yf.download(dropdown,start,end)['Adj Close']
    df = relativereturn(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)