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

        # Print the columns for debugging
        print(f"Fetched columns: {data.columns}")

        if data.empty:
            raise ValueError("No data fetched. Check the symbol or date range.")

        # Flatten multi-level columns if they exist
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [' '.join(col).strip() for col in data.columns]

        # Check for required columns
        required_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise KeyError(f"Missing columns in data: {missing_columns}")

        # Reset index to ensure 'Date' is a column
        data.reset_index(inplace=True)

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Insert data into the database
        for _, row in data.iterrows():
            # Extract scalar values
            date_str = row['Date'].strftime("%Y-%m-%d") if isinstance(row['Date'], pd.Timestamp) else row['Date']
            open_val = float(row['Open'])
            high_val = float(row['High'])
            low_val = float(row['Low'])
            close_val = float(row['Close'])
            adj_close_val = float(row['Adj Close'])
            volume_val = int(row['Volume'])

            # Debugging: Print the row being inserted
            print(f"Inserting row: symbol={symbol}, date={date_str}, open={open_val}, high={high_val}, "
                  f"low={low_val}, close={close_val}, adj_close={adj_close_val}, volume={volume_val}")
            print(f"Types: symbol={type(symbol)}, date={type(date_str)}, open={type(open_val)}, "
                  f"high={type(high_val)}, low={type(low_val)}, close={type(close_val)}, "
                  f"adj_close={type(adj_close_val)}, volume={type(volume_val)}")

            cursor.execute(
                """
                INSERT INTO historical_data (symbol, date, open, high, low, close, adj_close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    symbol,
                    date_str,  # Ensure this is a string
                    open_val,
                    high_val,
                    low_val,
                    close_val,
                    adj_close_val,
                    volume_val,
                )
            )

        conn.commit()
        conn.close()
        print("Data fetching and storage complete.")
        return data
    except KeyError as e:
        print(f"KeyError: {e}")
    except sqlite3.Error as e:
        print(f"SQLite error while inserting data: {e}")
    except Exception as e:
        print(f"Unexpected error while fetching data: {e}")
