from webull import webull

# Enter your Webull login info
USERNAME = 'TyFonze1'
PASSWORD = 'qYqpyw-4kidwa-hyvgus'

wb = webull()
wb.login(USERNAME, PASSWORD)
quote = wb.get_quote('AAPL')
print(quote)