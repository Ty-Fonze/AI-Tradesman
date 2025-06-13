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
            price = ticker.info.get('regularMarketPrice')
            name = ticker.info.get('shortName')
            return {
                "symbol": symbol,
                "price": price,
                "name": name,
                "exchange": "US",
                "realtime": False,
                "delay_minutes": 15
            }
        except Exception as e:
            return {"error": str(e)}
    return None