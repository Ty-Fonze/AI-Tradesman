import yfinance as yf
from redis_connection import connect_to_redis

# Fetch and store real-time stock data
def fetch_and_store_realtime_data(symbol):
    """
    Fetch real-time stock data using yfinance and store it in Redis.
    """
    redis_conn = connect_to_redis()
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d", interval="1m").tail(1)  # Fetch the latest minute's data

    if data.empty:
        print(f"No data found for {symbol}.")
        return

    latest = data.iloc[0]
    stock_data = {
        "symbol": symbol,
        "price": float(latest["Close"]),
        "volume": int(latest["Volume"]),
    }

    redis_key = f"realtime:{symbol}"
    redis_conn.set(redis_key, str(stock_data))
    redis_conn.expire(redis_key, 60)  # Set a TTL of 60 seconds
    print(f"Stored in Redis: {redis_key} -> {stock_data}")
