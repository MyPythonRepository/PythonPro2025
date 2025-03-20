from flask import Flask, jsonify
import requests
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


# http://localhost:5000/bitcoin_rate?currency=UAH&convert=10
@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.Str(missing="USD"),
        "convert": fields.Float(missing=1)
    },
    location="query"
)
def get_bitcoin_value(currency, convert):
    url = "https://bitpay.com/api/rates"
    rates = requests.get(url).json()

    rate = next(item["rate"] for item in rates if item["code"] == currency.upper())

    total_value = convert * rate

    return jsonify({
        "1. Currency code": currency.upper(),
        "2. BTC rate per 1 unit": round(rate, 2),
        "3. Amount of Bitcoin requested": round(convert, 2),
        "4. Converted total value": round(total_value, 2)
    })


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
