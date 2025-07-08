from flask import Flask, render_template, request
from utils import fetch_stock_data
from predictor import predict_next_days
from analyzer import analyze_trends
from reporter import generate_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()

        try:
            df = fetch_stock_data(ticker)
            if df.empty:
                return render_template("index.html", error="No data found for this ticker. Please try another.")

            predictions = predict_next_days(df)
            analysis = analyze_trends(df)
            report = generate_report(ticker, analysis["Trend"], analysis["RSI"], analysis["Note"])

            return render_template(
                "result.html",
                ticker=ticker,
                report=report,
                predictions=predictions
            )

        except Exception as e:
            return render_template("index.html", error=f"Something went wrong: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
