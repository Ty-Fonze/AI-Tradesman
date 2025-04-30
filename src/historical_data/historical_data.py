import os
import sqlite3
import yfinance as yf
import pandas as pd


def setup_database():
    """
    Sets up the SQLite database and initializes it with the schema from schema.sql.
    """
    # Determine the path to the schema.sql file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(base_dir, "schema.sql")

    try:
        print("Applying schema to database...")
        # Read the schema and apply it to the SQLite database
        with open(schema_path, "r") as schema_file:
            schema = schema_file.read()

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.executescript(schema)  # Apply the schema
        conn.commit()
        conn.close()
        print("Schema applied successfully.")
    except FileNotFoundError:
        print(f"Error: schema.sql file not found at {schema_path}")
    except sqlite3.Error as e:
        print(f"SQLite error while applying schema: {e}")
    except Exception as e:
        print(f"Unexpected error while applying schema: {e}")


def fetch_historical_data(symbol, start_date, end_date):
    """
    Fetches historical stock data for a given symbol and date range using Yahoo Finance.
    Ensures the 'Adj Close' column is included by setting auto_adjust=False.

    :param symbol: Stock ticker symbol (e.g., 'AAPL')
    :param start_date: Start date for data fetch (YYYY-MM-DD format)
    :param end_date: End date for data fetch (YYYY-MM-DD format)
    :return: Pandas DataFrame containing the historical data
    """
    try:
        print(f"Fetching data for {symbol}...")
        # Fetch data with auto_adjust=False to include 'Adj Close'
        data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=False)

        # Print the first few rows of the data to verify the structure
        print(data.head())

        if data.empty:
            raise ValueError("No data fetched. Check the symbol or date range.")

        # Check if 'Adj Close' exists
        if 'Adj Close' not in data.columns:
            raise ValueError("'Adj Close' column is missing in the data fetched. Check the stock symbol or date range.")

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Insert data into the database
        for index, row in data.iterrows():
            cursor.execute(
                """
                INSERT INTO historical_data (symbol, date, open, high, low, close, adj_close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    symbol,
                    index.strftime("%Y-%m-%d"),  # Convert date to string format
                    row['Open'],
                    row['High'],
                    row['Low'],
                    row['Close'],
                    row['Adj Close'],
                    int(row['Volume']) if not isinstance(row['Volume'], pd.Series) else int(row['Volume'].iloc[0]),
                )
            )

        conn.commit()
        conn.close()
        print("Data fetching and storage complete.")
        return data
    except KeyError as e:
        print(f"KeyError: Missing column in data: {e}")
    except sqlite3.Error as e:
        print(f"SQLite error while inserting data: {e}")
    except Exception as e:
        print(f"Unexpected error while fetching data: {e}")


if __name__ == "__main__":
    # Initialize the database
    setup_database()

    # Example: Fetch historical data for AAPL from 2022-01-01 to 2022-12-31
    symbol = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-12-31"

    # Fetch and store data
    data = fetch_historical_data(symbol, start_date, end_date)
