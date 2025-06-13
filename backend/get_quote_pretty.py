from webull import webull

USERNAME = 'TyFonze1'
PASSWORD = 'qYqpyw-4kidwa-hyvgus'

wb = webull()
wb.login(USERNAME, PASSWORD)
quote = wb.get_quote('AAPL')

print(f"Stock: {quote['name']} ({quote['symbol']})")
print(f"Price: ${quote['close']}")
print(f"Change: {float(quote['change']):+} ({float(quote['changeRatio'])*100:+.2f}%)")
print(f"Open: ${quote['open']}")
print(f"High: ${quote['high']}")
print(f"Low: ${quote['low']}")
print(f"Volume: {quote['volume']}")
print(f"52wk High: ${quote['fiftyTwoWkHigh']}")
print(f"52wk Low: ${quote['fiftyTwoWkLow']}")