import redis
import yfinance as yf
from datetime import datetime
import time

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
TTL = 86400  # Time-To-Live in seconds (24 hours)

def connect_to_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def fetch_realtime_data(symbol):
    """Fetch real-time stock data using yfinance."""
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d", interval="1m")
    if data.empty:
        print(f"No data found for {symbol}.")
        return None

    latest = data.iloc[-1]
    return {
        "symbol": symbol,
        "timestamp": datetime.now().isoformat(),
        "price": latest['Close'],
        "volume": int(latest['Volume'])
    }

def store_realtime_data(redis_conn, data):
    """Store real-time data in Redis with a TTL."""
    key = f"realtime:{data['symbol']}:{data['timestamp']}"
    redis_conn.setex(key, TTL, str(data))
    print(f"Stored: {key}")

if __name__ == "__main__":
    redis_conn = connect_to_redis()
    symbols = ["AAPL", "GOOGL", "MSFT"]  # Add your stock symbols here

    while True:
        for symbol in symbols:
            data = fetch_realtime_data(symbol)
            if data:
                store_realtime_data(redis_conn, data)
        time.sleep(60)  # Wait 1 minute before fetching again
