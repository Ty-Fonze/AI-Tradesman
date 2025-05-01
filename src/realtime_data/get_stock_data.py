from redis_connection import connect_to_redis

# Fetch stock data from Redis
def get_ticker_data(symbol):
    """
    Retrieve real-time stock data for a given symbol from Redis.
    """
    redis_conn = connect_to_redis()
    redis_key = f"realtime:{symbol}"
    data = redis_conn.get(redis_key)

    if data:
        print(f"Data for {symbol}: {data}")
        return data
    else:
        print(f"No data found for {symbol}.")
        return None
