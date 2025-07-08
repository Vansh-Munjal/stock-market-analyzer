# prediction.py
# Uses Linear Regression to predict next 5 days closing prices
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_days(df, days=5):
    """
    Predict future stock prices using linear regression.

    Parameters:
    - df (pd.DataFrame): DataFrame with 'Close' column
    - days (int): Number of future days to predict

    Returns:
    - List[float]: Predicted closing prices
    """
    df = df.copy()
    df['day_num'] = np.arange(len(df))

    X = df[['day_num']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(len(df), len(df) + days).reshape(-1, 1)
    predictions = model.predict(future_days)

    return predictions.tolist()
