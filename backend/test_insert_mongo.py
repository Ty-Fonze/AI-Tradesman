import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["StockData"]
collection = db["quotes"]

# Sample stock data
sample_stock = {
    "symbol": "AAPL",
    "timestamp": datetime.utcnow(),
    "price": 199.20,
    "volume": 44061396,
    "sector": "Technology",
    "industry": "Consumer Electronics"
}

# Insert data into MongoDB
collection.insert_one(sample_stock)

print("Inserted stock data into MongoDB!")
