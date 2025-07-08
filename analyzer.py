#RSI — Relative Strength Index (momentum)
#SMA(10) — Short-term trend (10-day Simple Moving Average)
#SMA(20) — Medium-term trend (20-day Simple Moving Average)

import pandas_ta as ta

def analyze_trends(df):
    result = {}
    df = df.copy()
    df.ta.rsi(length=14, append=True)
    df.ta.sma(length=10, append=True)
    df.ta.sma(length=20, append=True)

    rsi = df["RSI_14"].iloc[-1]
    ma10 = df["SMA_10"].iloc[-1]  #.iloc[-1] means: get the last (most recent) value.
    ma20 = df["SMA_20"].iloc[-1]

    #If RSI < 30 → stock is oversold → may bounce back
    result["RSI"] = rsi
    result["Trend"] = "Bullish" if ma10 > ma20 else "Bearish"
    result["Note"] = "Possibly oversold" if rsi < 30 else "Normal range"
    return result
