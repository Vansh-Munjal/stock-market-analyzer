# report.py
# Creates a plain English summary based on technical indicators and prediction

def generate_report(ticker, trend, rsi, note):
    """
    Create a readable stock report based on trend and RSI.

    Parameters:
    - ticker (str): Stock symbol
    - trend (str): 'Bullish' or 'Bearish'
    - rsi (float): Latest RSI value
    - note (str): Additional RSI interpretation

    Returns:
    - str: Multi-line formatted report
    """
    return (
        f"Stock: {ticker}\n"
        f"Trend: {trend}\n"
        f"RSI: {rsi:.2f} ({note})\n"
        f"Analysis: Based on the trend and RSI, "
        f"{'potential growth ahead' if trend == 'Bullish' else 'watch for downtrend'}."
    )
