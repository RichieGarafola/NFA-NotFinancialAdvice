# web development
import streamlit as st
import numpy as np
# Data Handling
import pandas as pd
from pathlib import Path
# Pull in financial information
import yfinance as yf 
# Read in API as a df format
import pandas_datareader.data as web
# Use the MinMaxScaler to scale data between 0 and 1.
from sklearn.preprocessing import MinMaxScaler
# Import required Keras modules
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
tickers_dropdown = st.selectbox('Choose a stock ticker', tickers)

# Load the stocks data
df = web.DataReader(tickers_dropdown, 'yahoo')[['Close']]

# The function has the following parameters:
# - df: The original DataFrame with the time series data.
# - window: The window size in days of previous closing prices that will be used for the prediction.
# - feature_col_number: The column number from the original DataFrame where the features are located.
# - target_col_number: The column number from the original DataFrame where the target is located.

def window_data(df, window, feature_col_number, target_col_number):
    """
    This function accepts the column number for the features (X) and the target (y).
    It chunks the data up with a rolling window of Xt - window to predict Xt.
    It returns two numpy arrays of X and y.
    """
    X = [] # The input features vectors.
    y = [] # The target vector
    for i in range(len(df) - window):
        features = df.iloc[i : (i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)


# Create the features (X) and target (y) data using the window_data() function.
# Have user input window size feature coulmn and target column 
# window_size = st.sidebar.text_input("The window size in days of previous closing prices that will be used for the prediction: ",  value=5)
window_size = 5
feature_column = 0
target_column = 0

X, y = window_data(df, window_size, feature_column, target_column)

# Splitting Data Between Training and Testing Sets
# To avoid the dataset being randomized, manually split the data using array slicing.
# Use 80% of the data for training and the remainder for testing
split = int(0.8 * len(X))
X_train = X[: split]
X_test = X[split:]
y_train = y[: split]
y_test = y[split:]

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit the MinMaxScaler object with the training feature data X_train
scaler.fit(X_train)

# Scale the features training and testing sets
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Fit the MinMaxScaler object with the training target data y_train
scaler.fit(y_train)

# Scale the target training and testing sets
y_train = scaler.transform(y_train)
y_test = scaler.transform(y_test)

# Reshape the features for the model
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))



# Define the LSTM RNN model.
model = Sequential()

number_units = 5
dropout_fraction = 0.2

# Layer 1
model.add(LSTM(
    units=number_units,
    return_sequences=True,
    input_shape=(X_train.shape[1], 1))
    )
model.add(Dropout(dropout_fraction))
# Layer 2
model.add(LSTM(units=number_units, return_sequences=True))
model.add(Dropout(dropout_fraction))
# Layer 3
model.add(LSTM(units=number_units))
model.add(Dropout(dropout_fraction))
# Output layer
model.add(Dense(1))

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Summarize the model
model.summary()

epochs = st.sidebar.number_input("The amount of epochs that will be used for the prediction: ",  value=15)
batch_size = st.sidebar.number_input("The batch size that will be used for the prediction: ",  value=64)
# Train the model
model.fit(X_train, y_train, epochs=epochs, shuffle=False, batch_size=batch_size, verbose=1)

# Evaluate the model
model.evaluate(X_test, y_test)

# Make some predictions
predicted = model.predict(X_test)

# Recover the original prices instead of the scaled version
predicted_prices = scaler.inverse_transform(predicted)
real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

# Create a DataFrame of Real and Predicted values
stocks = pd.DataFrame({
    "Real": real_prices.ravel(),
    "Predicted": predicted_prices.ravel()
    }, index = df.index[-len(real_prices): ])
stocks_df = stocks.sort_index(ascending=False)


# Plot the real vs predicted prices as a line chart
st.line_chart(stocks)

st.write(stocks_df)