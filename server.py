from flask import Flask, request, jsonify
from market_data_service import get_stock_price

app = Flask(__name__)

@app.route("/api/market/price", methods=["GET"])
def price():
    symbol = request.args.get("symbol")
    region = request.args.get("region", "US")
    if not symbol:
        return jsonify({"error": "symbol required"}), 400
    data = get_stock_price(symbol, region)
    if not data:
        return jsonify({"error": "not found"}), 404
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)