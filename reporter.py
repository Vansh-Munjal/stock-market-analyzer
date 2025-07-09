def generate_report(ticker, trend, rsi, note):
    """
    Generate a simple summary report for the stock based on technical indicators.
    This version does not use GPT; it's rule-based and fully offline.
    """

    # Header
    summary = f"📈 Stock Summary for {ticker}\n\n"
    
    # Trend line
    summary += f"• **Trend**: {trend.capitalize()}.\n"

    # RSI interpretation
    if rsi < 30:
        rsi_summary = "RSI is below 30, suggesting the stock may be oversold and could experience a price rebound."
    elif rsi > 70:
        rsi_summary = "RSI is above 70, indicating the stock might be overbought and due for a pullback."
    else:
        rsi_summary = "RSI is between 30 and 70, which is considered a normal range showing stable momentum."

    summary += f"• **RSI**: {rsi} → {rsi_summary}\n"

    # Additional analysis
    summary += f"• **Note**: {note.strip()}"

    return summary
