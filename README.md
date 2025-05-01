# 📈 AI Tradesman - Your Stock Market Assistant

AI Tradesman is an AI-powered assistant designed to empower traders with smarter decision-making capabilities. By leveraging real-time market data, technical analysis, and advanced AI tools, it provides actionable insights for traders.

---

## 🚀 Features
- **Market Scanning**: Identify high-performing or underperforming stocks using technical and fundamental indicators.
- **Multi-Timeframe Analysis**: Analyze trends across daily, 4-hour, and 15-minute charts.
- **Real-Time Insights**: Detect market regimes (bullish, bearish, or sideways) and adapt strategies.
- **Redis-Based Real-Time Monitoring**: Fetch and store stock data in Redis for periodic updates and alerts.
- **Sector Analysis**: Track sector performance and correlations between stocks and indices.
- **Interactive Dashboard**: Visualize insights and interact with AI-generated recommendations.
- **Educational Guidance**: Learn trading strategies with mentor-mode explanations and tips.

---

## 🛠️ Installation and Setup

### Prerequisites
1. Install Python (≥ 3.8) and Node.js (≥ 14.x).
2. Obtain API keys from stock data providers (e.g., Alpha Vantage, Yahoo Finance).
3. Ensure that a Redis server is running locally or remotely.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ty-Fonze/AI-Tradesman.git
   cd AI-Tradesman
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: The `yfinance` library is included in the `requirements.txt` file and is used to fetch stock market data with a slight delay (up to 15 minutes for the free tier).

3. Install additional dependencies for real-time monitoring:
   ```bash
   pip install -r src/realtime_data/requirements.txt
   ```

4. Install Node.js dependencies:
   ```bash
   cd src/dashboard
   npm install
   ```

5. Configure API keys:
   - Copy `config/api_keys_template.json` to `config/api_keys.json`.
   - Add your API keys.

6. Run the backend:
   ```bash
   python src/dashboard/app.py
   ```

7. Start the frontend:
   ```bash
   cd src/dashboard
   npm start
   ```

---

## 💡 Usage

### Real-Time Monitoring
The Redis-based real-time monitoring module fetches live stock data, stores it in Redis, and triggers alerts based on predefined thresholds.

1. Start the monitoring script:
   ```bash
   python src/realtime_data/main.py
   ```
   - This will fetch stock data periodically and store it in Redis.

2. Check for alerts:
   - Alerts will be printed to the console if a stock price exceeds a threshold.
   - Example:
     ```
     🚨 Alert: AAPL price is above 175 -> 176.5
     ```

3. Verify Redis storage:
   - Use `redis-cli` to inspect stored data:
     ```bash
     redis-cli
     keys *
     ```

---

## 🛠️ Data Fetching and Database

### Data Fetching with Yahoo Finance (`yfinance`)
The system uses the `yfinance` library as its primary data provider for stock market data. Note that the data may have a 15-minute delay due to Yahoo Finance's limitations in the free tier.

- **Historical Data**: The script fetches historical stock data using `yfinance` and stores it in a local SQLite database (`tradesman.db`).
- **Real-Time Data**: Real-time stock data is fetched and stored in Redis for fast access and periodic updates.

### Example Usage
Here’s an example of how to fetch and store historical data programmatically:
```python
from src.historical_data.historical_data import fetch_and_store_data

# Fetch and store data for Apple stock from 2022 to 2023
fetch_and_store_data("AAPL", "2022-01-01", "2023-01-01")
```

To simulate real-time updates:
```python
from src.historical_data.historical_data import simulate_realtime

simulate_realtime("AAPL")
```

---

## 📅 Roadmap
- **Phase 1**: Core features like market scanning, data analysis, and multi-timeframe insights.
- **Phase 2**: Advanced tools such as sector analysis and heatmaps.
- **Phase 3**: Redis-based real-time monitoring and alerting system. ✅
- **Phase 4**: Interactive tools like scenario simulations and emotional decision trackers.
- **Phase 5**: Personalization and educational features such as mentor mode.

---

## 🤝 Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your branch and open a pull request.

---

## 📜 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

---

## 📬 Contact
For questions, feedback, or support, reach out to [Ty-Fonze](https://github.com/Ty-Fonze).
