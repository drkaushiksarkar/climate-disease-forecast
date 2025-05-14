from sklearn.ensemble import IsolationForest

def detect_anomalies(df, target):
    df = df[[target]].dropna()
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[[target]])
    df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})
    return df