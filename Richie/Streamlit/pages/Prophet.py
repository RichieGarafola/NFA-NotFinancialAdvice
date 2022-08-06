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
st.title("NotFinanialAdvice Streamlit Finance Dashboard")

tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
dropdown = st.selectbox('Pick your asset', tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

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
forecast_dow = model_dow.predict(future_dow)
# Plot predictions for our forecast_dow DataFrame for the 52 week period 
forecast_dow_predictions = forecast_dow[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:]

# Use the plot_components function to visualize the forecast results 
figures = model_dow.plot_components(forecast_dow)

# Create a `forecast_future_month` Dataframe, which contains just forecasts for the future
# The DataFrame should include the columns yhat_upper, yhat_lower, and yhat

end = pd.to_datetime('today').strftime('%Y-%m-%d')
time_delta = dt.timedelta(days = 20)
start = (pd.to_datetime(end) - time_delta).strftime('%Y-%m-%d')

forecast_future_month = forecast_dow.loc[start:end][["yhat_upper", "yhat_lower", "yhat"]]

# Replace the column names to something less technical sounding
forecast_future_month = forecast_future_month.rename(
    columns={
        "yhat_upper": "Best Case",
        "yhat_lower": "Worst Case", 
        "yhat": "Most Likely Case"
    }
)


# Dashboard 
st.title("Prophet Forecast")
st.pyplot(model_dow.plot(forecast_dow))

st.title(f"{dropdown} Prophet Forecast Predictions")
fig, ax = plt.subplots()
ax.plot(forecast_dow_predictions)
ax.legend(['yhat', 'yhat_lower', 'yhat_upper'])
st.pyplot(fig)

st.pyplot(figures)

# Review the last five rows of the DataFrame
st.write(forecast_future_month.tail())

# Display the average forecasted price 
st.write(forecast_future_month.mean())
