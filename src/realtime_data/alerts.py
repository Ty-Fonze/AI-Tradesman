from get_stock_data import get_ticker_data

# Check for alerts
def check_alerts(symbol, threshold):
    """
    Check if the stock price exceeds the threshold.
    """
    data = get_ticker_data(symbol)

    if data:
        price = float(eval(data)["price"])  # Extract price from stored data
        if price >= threshold:
            print(f"🚨 Alert: {symbol} price is above {threshold} -> {price}")
    else:
        print(f"No data available for {symbol}. Skipping alert check.")
