import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

def plot_stl(df, target):
    df = df.set_index('date')
    stl = STL(df[target], period=52).fit()
    return stl.trend, stl.seasonal, stl.resid