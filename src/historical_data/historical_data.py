import yfinance as yf
import pandas as pd
import sqlite3
import os

DATABASE_FILE = "tradesman.db"

def apply_schema():
    """Applies the database schema if it doesn't exist already."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Example schema (adjust columns/types based on your needs)
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
    data = yf.download(ticker, start=start_date, end=end_date)

    # Check for required columns before proceeding
    required_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    missing = [col for col in required_columns if col not in data.columns]
    if missing:
        raise KeyError(f"Missing column(s) in data: {missing}")

    data.reset_index(inplace=True)
    data["Ticker"] = ticker

    # Rename columns to match schema
    data.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume",
        "Date": "date"
    }, inplace=True)

    # Store in SQLite
    connection = sqlite3.connect(DATABASE_FILE)
    data.to_sql("stock_data", connection, if_exists="append", index=False)
    connection.close()

def main():
    if not os.path.exists(DATABASE_FILE):
        print("Applying schema to database...")
        apply_schema()

    # Example usage
    ticker_symbol = "AAPL"
    start = "2022-01-01"
    end = "2023-01-01"

    fetch_and_store_data(ticker_symbol, start, end)

if __name__ == "__main__":
    main()
