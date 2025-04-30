import sqlite3
import yfinance as yf
from datetime import datetime, timedelta

DB_PATH = "stock_data.db"

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open("schema.sql", "r") as schema_file:
        cursor.executescript(schema_file.read())
    conn.commit()
    conn.close()

def fetch_historical_data(symbol, start_date, end_date):
    """Fetch historical stock data using yfinance."""
    data = yf.download(symbol, start=start_date, end=end_date)
    if data.empty:
        print(f"No data found for {symbol}.")
        return []

    records = []
    for date, row in data.iterrows():
        records.append((
            symbol, date.strftime('%Y-%m-%d'), row['Open'], row['High'],
            row['Low'], row['Close'], row['Adj Close'], int(row['Volume'])
        ))
    return records

def store_historical_data(data):
    """Store historical data into SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT OR IGNORE INTO historical_data
        (symbol, date, open, high, low, close, adjusted_close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    symbols = ["AAPL", "GOOGL", "MSFT"]  # Add your stock symbols here
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=730)).strftime('%Y-%m-%d')  # Last 2 years

    for symbol in symbols:
        print(f"Fetching data for {symbol}...")
        data = fetch_historical_data(symbol, start_date, end_date)
        if data:
            store_historical_data(data)
            print(f"Stored data for {symbol}.")
