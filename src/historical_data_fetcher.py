import yfinance as yf
import pandas as pd

class HistoricalDataFetcher:
    def __init__(self, symbol):
        """
        Initialize the historical data fetcher with a stock symbol.
        :param symbol: The stock ticker symbol (e.g., "AAPL" for Apple).
        """
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_historical_data(self, period="1y", interval="1d"):
        """
        Fetch historical stock data for a given period and interval.
        :param period: The period of data (e.g., "1d", "5d", "1mo", "1y").
        :param interval: The data interval (e.g., "1m", "5m", "1h", "1d").
        :return: A Pandas DataFrame with historical data.
        """
        return self.ticker.history(period=period, interval=interval)

    def save_to_csv(self, data, filename):
        """
        Save the historical data to a CSV file.
        :param data: The Pandas DataFrame containing the historical data.
        :param filename: The name of the CSV file to save the data.
        """
        data.to_csv(filename)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    fetcher = HistoricalDataFetcher("AAPL")  # Replace "AAPL" with the stock symbol you want
    historical_data = fetcher.get_historical_data()
    print(historical_data)
    fetcher.save_to_csv(historical_data, "historical_data.csv")
