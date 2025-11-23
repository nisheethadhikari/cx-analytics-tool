import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_volume(df, date_col="CreatedDate", period=12):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    ts = df[date_col].dt.to_period("M").value_counts().sort_index().to_timestamp()
    model = ExponentialSmoothing(ts, trend="add", seasonal="add", seasonal_periods=12)
    fit = model.fit()
    forecast = fit.forecast(period)
    return forecast