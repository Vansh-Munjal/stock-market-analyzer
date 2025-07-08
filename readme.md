# 📊 Stock Market Analyzer

A simple Flask web app that:
- Fetches live stock data using `yfinance`
- Predicts next 5 days' closing prices using Linear Regression
- Performs RSI and Moving Average analysis with `pandas-ta`
- Generates a natural-language report

## 🔧 Tech Stack

- **Python** (Flask)
- **HTML + CSS**
- **Machine Learning** (Linear Regression)
- **APIs**: yfinance
- **Indicators**: RSI, SMA

## 📦 Setup

```bash
git clone https://github.com/your-username/stock-market-analyzer.git
cd stock-market-analyzer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
