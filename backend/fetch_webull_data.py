from webull import webull
import pymongo
from datetime import datetime

# Webull login setup
wb = webull()
wb.login('your_email', 'your_password')

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["StockData"]
collection = db["quotes"]

# Fetch real-time stock data
symbol = "TSLA"
stock_data = wb.get_quote(symbol)

# Format data for MongoDB
formatted_data = {
    "symbol": symbol,
    "timestamp": datetime.utcnow(),
    "price": stock_data['close'],
    "volume": stock_data['volume'],
    "sector": "Consumer Cyclical",  # Placeholder, fetch dynamically if needed
    "industry": "Automotive"
}

# Insert into MongoDB
collection.insert_one(formatted_data)

print(f"Inserted Webull stock data for {symbol} into MongoDB!")
