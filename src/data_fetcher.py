import yfinance as yf

class YahooFinanceFetcher:
    def __init__(self, symbol):
        """
        Initialize the data fetcher with a stock symbol.
        :param symbol: The stock ticker symbol (e.g., "AAPL" for Apple).
        """
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_latest_price(self):
        """
        Fetch the latest stock price.
        :return: The latest stock price as a float.
        """
        data = self.ticker.history(period="1d", interval="1m")
        latest_data = data.tail(1)
        return latest_data['Close'].iloc[0] if not latest_data.empty else None

    def get_historical_data(self, period="5d", interval="1h"):
        """
        Fetch historical stock data for a given period and interval.
        :param period: The period of data (e.g., "1d", "5d", "1mo").
        :param interval: The data interval (e.g., "1m", "5m", "1h", "1d").
        :return: A Pandas DataFrame with historical data.
        """
        return self.ticker.history(period=period, interval=interval)

# Example Usage
if __name__ == "__main__":
    fetcher = YahooFinanceFetcher("AAPL")  # Apple Inc.
    print("Latest Price:", fetcher.get_latest_price())
    print("Historical Data (5 days, 1-hour interval):")
    print(fetcher.get_historical_data())
