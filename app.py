from flask import Flask, render_template, request
from utils import fetch_stock_data
from predictor import predict_next_days
from analyzer import analyze_trends
from reporter import generate_report
import os
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        try:
            df = fetch_stock_data(ticker)
            if df.empty:
                return render_template("index.html", error="No data found for this ticker.", charts=get_top_charts())

            # Ensure datetime index
            df.index = pd.to_datetime(df.index)

            # Prediction
            predictions = predict_next_days(df)

            # Technical analysis and GPT summary
            analysis = analyze_trends(df)
            report = generate_report(ticker, analysis["Trend"], analysis["RSI"], analysis["Note"])

            # Last 15 days history
            recent_data = df.tail(15)[['Open', 'Close', 'High', 'Low', 'Volume']].copy()
            recent_data["Date"] = recent_data.index.strftime("%Y-%m-%d")
            history = recent_data.to_dict(orient="records")

            return render_template(
                "result.html",
                ticker=ticker,
                report=report,
                analysis=analysis,
                predictions=predictions,
                history=history
            )

        except Exception as e:
            return render_template("index.html", error=f"Something went wrong: {str(e)}", charts=get_top_charts())

    return render_template("index.html", charts=get_top_charts())


# Helper function: Loads all stock charts (except prediction)
def get_top_charts():
    chart_dir = os.path.join("static", "charts")
    if not os.path.exists(chart_dir):
        return []

    files = os.listdir(chart_dir)
    charts = []
    for f in files:
        if f.endswith(".png") and f != "prediction.png":
            ticker = os.path.splitext(f)[0]
            charts.append({
                "ticker": ticker.upper(),
                "filename": f
            })
    return charts


if __name__ == "__main__":
    app.run(debug=True)
