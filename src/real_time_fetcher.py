import yfinance as yf

class RealTimeFetcher:
    def __init__(self, symbol):
        """
        Initialize the real-time data fetcher with a stock symbol.
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

# Example usage
if __name__ == "__main__":
    fetcher = RealTimeFetcher("AAPL")  # Replace "AAPL" with the stock symbol you want to track
    print("Latest Price:", fetcher.get_latest_price())
