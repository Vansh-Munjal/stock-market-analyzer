import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_next_days(df):
    df = df.copy()
    df = df.reset_index()

    df = df[['Date', 'Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days

    X = df[['Days']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    # Predict next 5 days
    last_day = df['Days'].max()
    future_days = pd.DataFrame({'Days': [last_day + i for i in range(1, 6)]})
    future_dates = [df['Date'].max() + pd.Timedelta(days=i) for i in range(1, 6)]
    future_pred = model.predict(future_days)

    # Return list of dicts with date and predicted price
    return [
        {"Date": future_dates[i].strftime("%Y-%m-%d"), "Predicted Price": round(future_pred[i], 2)}
        for i in range(5)
    ]
