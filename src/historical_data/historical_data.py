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
    CREATE TABLE IF NOT EXISTS historical_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        date DATE NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        adj_close REAL,
        volume INTEGER,
        UNIQUE(symbol, date)
    );
    """
    cursor.execute(schema_sql)
    connection.commit()
    connection.close()
    print("Schema applied successfully.")

def fetch_and_store_data(ticker, start_date, end_date):
    """Fetches historical data for a given ticker and date range, then stores it in the SQLite database."""
    print(f"Fetching data for {ticker}...")
    # Fetch data with auto_adjust=False to include 'Adj Close'
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)

    # Flatten multi-level columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    print("Columns fetched:", data.columns)

    # Ensure 'Adj Close' column exists, and if not, set it equal to 'Close'
    if "Adj Close" not in data.columns:
        print("'Adj Close' column is missing. Falling back to 'Close'.")
        data["Adj Close"] = data["Close"]

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

    data["symbol"] = ticker

    # Insert data into SQLite
    connection = sqlite3.connect(DATABASE_FILE)
    data.to_sql("historical_data", connection, if_exists="append", index=False)
    connection.close()

    print(f"Data for {ticker} from {start_date} to {end_date} stored successfully.")

def main():
    if not os.path.exists(DATABASE_FILE):
        print("Applying schema to database...")
        apply_schema()

    ticker_symbol = "AAPL"
    start = "2022-01-01"
    end = "2025-04-30"

    fetch_and_store_data(ticker_symbol, start, end)

if __name__ == "__main__":
    main()
