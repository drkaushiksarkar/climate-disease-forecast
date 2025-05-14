import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.ensemble import RandomForestRegressor
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

def sarimax_forecast(df, target):
    df = df[['date', target]].copy()

    # Drop duplicates by averaging same-date entries (if needed)
    df = df.groupby('date').mean().reset_index()

    # Set date index and set frequency
    df = df.set_index('date')
    df = df.asfreq('W')  # assumes weekly data

    model = SARIMAX(df[target], order=(1,1,1), seasonal_order=(1,1,1,52)).fit(disp=False)
    forecast = model.forecast(12)
    return forecast

def random_forest_forecast(df, target):
    df = df.dropna()
    X = df[['temperature', 'rainfall', 'humidity', 'ndvi', 'soil_moisture']]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)
    model = RandomForestRegressor().fit(X_train, y_train)
    preds = model.predict(X_test)
    return preds, y_test

def lstm_forecast(df, target):
    df = df[[target]].dropna()
    data = df.values
    X, y = [], []
    for i in range(10, len(data)):
        X.append(data[i-10:i, 0])
        y.append(data[i, 0])
    X = np.array(X)
    y = np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(X.shape[1], 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, verbose=0)
    return model.predict(X[-12:])