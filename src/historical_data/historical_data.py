import yfinance as yf
import pandas as pd
import sqlite3
import os

DATABASE_FILE = "tradesman.db"

def apply_schema():
    """Applies the database schema if it doesn't exist already."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    schema_sql = """
    CREATE TABLE IF NOT EXISTS stock_data (
        date TEXT,
        ticker TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        adj_close REAL,
        volume INTEGER
    )
    """
    cursor.execute(schema_sql)
    connection.commit()
    connection.close()
    print("Schema applied successfully.")

def fetch_and_store_data(ticker, start_date, end_date):
    """Fetches historical data for a given ticker and date range, then stores it in the SQLite database."""
    print(f"Fetching data for {ticker}...")
    # Set auto_adjust=False so 'Adj Close' is included
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)

    # Flatten multi-level columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    print("Columns:", data.columns)

    # Copy the current index to a 'date' column first
    data["date"] = data.index

    # Then reset the index (dropping the old index)
    data.reset_index(drop=True, inplace=True)

    # Rename columns to match the database schema
    data.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    }, inplace=True, errors="ignore")

    # Confirm required columns
    required_columns = ["date", "open", "high", "low", "close", "adj_close", "volume"]
    missing = [col for col in required_columns if col not in data.columns]
    if missing:
        raise KeyError(f"Missing column(s) in data after rename: {missing}")

    data["ticker"] = ticker

    # Insert data into SQLite
    connection = sqlite3.connect(DATABASE_FILE)
    data.to_sql("stock_data", connection, if_exists="append", index=False)
    connection.close()

def main():
    if not os.path.exists(DATABASE_FILE):
        print("Applying schema to database...")
        apply_schema()

    ticker_symbol = "AAPL"
    start = "2022-01-01"
    end = "2023-01-01"

    fetch_and_store_data(ticker_symbol, start, end)

if __name__ == "__main__":
    main()
