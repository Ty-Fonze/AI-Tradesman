import redis
import sqlite3
import json
from datetime import datetime

DB_PATH = "stock_data.db"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

def connect_to_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def fetch_keys(redis_conn, pattern="realtime:*"):
    """Fetch all keys matching a pattern."""
    return redis_conn.keys(pattern)

def move_to_sqlite(redis_conn, keys):
    """Move selected real-time data from Redis to SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for key in keys:
        data = json.loads(redis_conn.get(key))
        cursor.execute("""
            INSERT OR IGNORE INTO historical_data
            (symbol, date, open, high, low, close, adjusted_close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (data['symbol'], data['timestamp'].split("T")[0], None, None, None,
              data['price'], None, data['volume']))
        redis_conn.delete(key)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    redis_conn = connect_to_redis()
    keys = fetch_keys(redis_conn)

    if keys:
        move_to_sqlite(redis_conn, keys)
        print(f"Moved {len(keys)} records from Redis to SQLite.")
