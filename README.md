# 📈 AI Tradesman - Your Stock Market Assistant

AI Tradesman empowers traders with AI-driven insights, real-time data, and an interactive dashboard for smarter decision-making.

---

## 🚀 Features
- **Market Scanning**: Identify top gainers/losers using technical and fundamental indicators.  
- **Multi-Timeframe Analysis**: Trends on daily, 4-hour, and 15-minute charts.  
- **Real-Time Alerts**: Threshold-based alerts via Redis and notifications.  
- **Sector & Correlation Analysis**: Track sector performance and stock-index correlations.  
- **Interactive Dashboard**: React/Electron UI with movable widgets and AI recommendations.  
- **Educational Mentor Mode**: In-depth explanations of strategies and indicators.

---

## 🏗️ Current Progress

### MongoDB Integration
- Installed MongoDB & MongoDB Compass  
- Added MongoDB `bin` to system PATH  
- Verified `mongod` runs on port 27017  
- Inserted test stock data (`AAPL`, `TSLA`) via Python scripts  
- Confirmed data in MongoDB Compass  

### Backend
- **AI Engine**: Ready for frontend integration  
- **Real-Time Monitoring**: Redis-based data fetch & alerting  
- **Data Storage**:  
  - Historical data in SQLite  
  - Real-time snapshots in Redis  
  - Structured stock data in MongoDB  

### Frontend
- **React/Electron Dashboard**: Base UI implemented  
- **Widgets**: `LiveTickerWidget` functional  
- **To-Do**:  
  - Add `public/index.html` for frontend build  
  - Integrate AI backend endpoints  

---

## 🛠️ Installation & Setup

### Prerequisites
- Python ≥ 3.8  
- Node.js ≥ 14.x  
- MongoDB Server (8.x) & MongoDB Compass  
- Redis Server  
- API keys for chosen data providers

### Setup Steps
1. **Clone the repo**  
   ```bash
   git clone https://github.com/Ty-Fonze/AI-Tradesman.git
   cd AI-Tradesman

Python dependencies

pip install -r requirements.txt

Redis dependencies

pip install -r src/realtime_data/requirements.txt

Node.js dependencies

cd src/dashboard
npm install

Configure API keys

cp config/api_keys_template.json config/api_keys.json
# Edit config/api_keys.json with your keys

MongoDB

Create data directory:

mkdir C:\data\db

Start MongoDB:

mongod --dbpath C:\data\db

(Optional) Connect with Compass: mongodb://localhost:27017

💡 Testing MongoDB

Insert Test Data

cd backend
python test_insert_mongo.py
python test_insert_mongo_2.py

Verify in Compass

Database: StockData

Collection: quotes

⚙️ Next Milestones

Automate real-time Webull data ingestion → MongoDB

Enhance stock query APIs

Refine MongoDB schema (indexes, partitions)

Build AI-driven recommendation widgets

Deploy full stack (Electron + Python)

🤝 Contributing

Fork & branch

Commit changes

Open a PR

📜 License

MIT License. See LICENSE.

📬 Contact

Questions or feedback? Reach out to Ty-Fonze.
