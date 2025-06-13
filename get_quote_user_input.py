from webull import webull

USERNAME = 'TyFonze1'
PASSWORD = 'qYqpyw-4kidwa-hyvgus'

wb = webull()
wb.login(USERNAME, PASSWORD)

symbol = input("Enter a stock symbol (e.g., AAPL, TSLA, MSFT): ").upper()
quote = wb.get_quote(symbol)

if 'name' in quote:
    print(f"Stock: {quote['name']} ({quote['symbol']})")
    print(f"Price: ${quote['close']}")
    print(f"Change: {float(quote['change']):+} ({float(quote['changeRatio'])*100:+.2f}%)")
    print(f"Open: ${quote['open']}")
    print(f"High: ${quote['high']}")
    print(f"Low: ${quote['low']}")
    print(f"Volume: {quote['volume']}")
else:
    print(f"Couldn't find data for symbol: {symbol}")