import yfinance as yf
import pandas as pd

class HistoricalDataFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_historical_data(self, period="1y", interval="1d"):
        return self.ticker.history(period=period, interval=interval)

    def save_to_csv(self, data, filename):
        data.to_csv(filename)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    fetcher = HistoricalDataFetcher("AAPL")
    historical_data = fetcher.get_historical_data()
    print(historical_data)
    fetcher.save_to_csv(historical_data, "historical_data.csv")
