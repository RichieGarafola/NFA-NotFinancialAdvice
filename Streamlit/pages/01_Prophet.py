import streamlit as st # web development
import pandas as pd # read csv, df manipulation
import matplotlib.pyplot as plt # plots 
import datetime as dt # Date time format
from plotly import graph_objs as go
from prophet import Prophet
import yfinance as yf

st.set_page_config(
    page_title="NotFinancialAdvice - Prophet",
    page_icon="📊",
    layout= "wide"    
)

# dashboard title
# st.title("NotFinanialAdvice Streamlit Finance Dashboard")
st.title("NotFinanialAdvice")


tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
dropdown = st.sidebar.selectbox('Pick your asset', tickers)

start = st.sidebar.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.sidebar.date_input('End', value = pd.to_datetime('today'))

df = yf.download(dropdown,start,end).Close

# Create a Prophet model for model_dow
model_dow = Prophet(yearly_seasonality=True)

# format 'dow_prophet_model' to fit the prophet functions parameters. 
dow_prophet_model = df.reset_index()
dow_prophet_model.columns = ['ds', 'y']

# Fit the Prophet model for dow data
model_dow.fit(dow_prophet_model)

# Forecast one year of weekly future trends data for the Future dow Closing Prices 
future_dow = model_dow.make_future_dataframe(periods=52, freq="W")

# Make predictions for forecast_dow using the future_dow DataFrame
forecast_dow = model_dow.predict(future_dow).set_index('ds')
foreccast_dow_figures = forecast_dow.reset_index()

# Plot predictions for our forecast_dow DataFrame for the 52 week period 
forecast_dow_predictions = forecast_dow[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:]

# Use the plot_components function to visualize the forecast results 
figures = model_dow.plot_components(foreccast_dow_figures)

# # Set the datetime index of the forecast_dow data, using the ds column
# forecast_dow_index = forecast_dow.set_index("ds")


start = pd.to_datetime('today').strftime('%Y-%m-%d')
time_delta = dt.timedelta(days = 20)
end = (pd.to_datetime(start) + time_delta).strftime('%Y-%m-%d')

forecast_future_month = forecast_dow.loc[start:end][["yhat_upper", "yhat_lower", "yhat"]]

# Replace the column names to something less technical sounding
forecast_future_month = forecast_future_month.rename(
    columns={
        "yhat_upper": "Best Case",
        "yhat_lower": "Worst Case", 
        "yhat": "Most Likely Case"
    }
)

############################################
# Dashboard 

############################################
# plot 1 not sccaled 
# st.title("Prophet Forecast")
# st.pyplot(model_dow.plot(foreccast_dow_figures))

# plot 2 not scaled
# st.title(f"{dropdown} Prophet Forecast Predictions")
# fig, ax = plt.subplots()
# ax.plot(forecast_dow_predictions)
# ax.legend(['yhat', 'yhat_lower', 'yhat_upper'])
# st.pyplot(fig)

# plot 3 not scaled 
# st.pyplot(figures)

st.header(f"{dropdown} Prophet Forecast Predictions")
fig, ax = plt.subplots()
ax.plot(forecast_dow_predictions)
ax.legend(['yhat', 'yhat_lower', 'yhat_upper'])

col1, col2, col3 = st.columns(3)

col1.subheader(f"{dropdown} Prophet Forecast")
col1.pyplot(model_dow.plot(foreccast_dow_figures))

col2.subheader(f"{dropdown} Prophet Forecast Predictions")
col2.pyplot(fig)

col3.subheader("Prophet Trends")
col3.pyplot(figures)



col1, col2 = st.columns(2)

col1.subheader("3 week forecast")
col1.write(forecast_future_month)

col2.subheader("Average Forecasted price for the next 21 days")
col2.write(forecast_future_month.mean())


# # Review the last five rows of the DataFrame
# st.write("The last 5 days",forecast_future_month.tail())

# # Display the average forecasted price 
# st.write("Average Forecasted price for the last 20 days", forecast_future_month.mean())

