import yfinance as yf
import matplotlib.pyplot as plt
import os

# Ensure directory exists
os.makedirs("static/charts", exist_ok=True)

tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

for ticker in tickers:
    data = yf.download(ticker, period="6mo")
    plt.figure(figsize=(10, 4))
    plt.plot(data["Close"], label="Close Price", color="blue")
    plt.title(f"{ticker} - Last 6 Months")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"static/charts/{ticker}.png")
    plt.close()
