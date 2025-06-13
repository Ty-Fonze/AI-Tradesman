import yfinance as yf
import akshare as ak

def get_stock_price(symbol: str, region: str = "US"):
    if region.upper() == "CN":
        try:
            df = ak.stock_zh_a_spot()
            row = df[df['代码'] == symbol]
            if not row.empty:
                return {
                    "symbol": symbol,
                    "price": float(row.iloc[0]['最新价']),
                    "name": row.iloc[0]['名称'],
                    "exchange": "CN",
                    "realtime": True,
                    "delay_minutes": 0
                }
        except Exception as e:
            return {"error": str(e)}
    else:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            price = None
            if not hist.empty:
                price = hist['Close'][0]
            name = symbol
            # Try to get name from either fast_info or info
            if hasattr(ticker, "fast_info") and getattr(ticker, "fast_info", None):
                name = ticker.fast_info.get("shortName", symbol)
            elif hasattr(ticker, "info") and ticker.info:
                name = ticker.info.get('shortName', symbol)
            if price is not None:
                return {
                    "symbol": symbol,
                    "price": float(price),
                    "name": name,
                    "exchange": "US",
                    "realtime": False,
                    "delay_minutes": 15
                }
            else:
                return {"error": "Price data not found for symbol"}
        except Exception as e:
            return {"error": str(e)}
    return None