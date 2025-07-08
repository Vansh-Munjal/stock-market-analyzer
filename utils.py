#Fetch historical stock data 
#yfinance is a Python library that lets you fetch historical market data from Yahoo Finance — like stock prices, volumes, dividends, and more.
#yfinance is a data-fetching library — it connects your Python code to live financial data from Yahoo Finance.

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="3mo", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Parameters:
    - ticker (str): Stock symbol, e.g., 'AAPL'
    - period (str): Data range (default "3mo")
    - interval (str): Data interval (default "1d")

    Returns:
    - pd.DataFrame: Historical stock data with Date, Open, Close, etc.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    hist.reset_index(inplace=True)
    return hist
