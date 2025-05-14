import streamlit as st
import pandas as pd
from utils.data_generator import generate_synthetic_data
from models.forecasting import sarimax_forecast, random_forest_forecast, lstm_forecast
from models.hotspot import cluster_hotspots
from models.anomaly import detect_anomalies
from utils.visualizations import plot_stl

# Load or generate data
@st.cache_data
def load_data():
    return pd.read_csv("data/synthetic_data.csv", parse_dates=['date'])

df = load_data()

st.title("Climate Sensitive Disease Forecasting Dashboard")

disease = st.sidebar.selectbox("Select Disease", ["Malaria", "Dengue", "Diarrhoea"])
upazila = st.sidebar.selectbox("Select Upazila", df['upazila'].unique())
target = {
    "Malaria": "malaria_api",
    "Dengue": "dengue_incidence",
    "Diarrhoea": "diarrhoea_incidence"
}[disease]

filtered = df[df['upazila'] == upazila].sort_values('date')

if disease in ["Malaria", "Dengue"]:
    st.subheader("STL Decomposition")
    trend, seasonal, resid = plot_stl(filtered, target)
    st.line_chart(trend.rename("Trend"))
    st.line_chart(seasonal.rename("Seasonality"))

    st.subheader("Forecasting Models")
    st.line_chart(sarimax_forecast(filtered, target).rename("SARIMAX Forecast"))

    preds, y_true = random_forest_forecast(filtered, target)
    st.line_chart(pd.Series(preds[-12:], name="Random Forest Forecast"))

    st.line_chart(pd.Series(lstm_forecast(filtered, target).flatten(), name="LSTM Forecast"))

if disease == "Diarrhoea" or disease in ["Malaria", "Dengue"]:
    st.subheader("Hotspot Clustering")
    clustered = cluster_hotspots(df[df['date'] > '2023-01-01'], target)
    st.map(clustered)

st.subheader("Anomaly Detection")
anomalies = detect_anomalies(filtered, target)
st.line_chart(anomalies[[target]])
st.scatter_chart(anomalies[anomalies['anomaly'] == 1][[target]])