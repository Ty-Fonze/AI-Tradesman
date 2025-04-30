import yfinance as yf

class RealTimeFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_latest_price(self):
        data = self.ticker.history(period="1d", interval="1m")
        latest_data = data.tail(1)
        return latest_data['Close'].iloc[0] if not latest_data.empty else None

# Example usage
if __name__ == "__main__":
    fetcher = RealTimeFetcher("AAPL")
    print("Latest Price:", fetcher.get_latest_price())
