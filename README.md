# 📈 AI Tradesman - Your Stock Market Assistant

AI Tradesman is an AI-powered assistant designed to empower traders with smarter decision-making capabilities. By leveraging real-time market data, technical analysis, and advanced AI tools, it provides actionable insights for traders.

---

## 🚀 Features
- **Market Scanning**: Identify high-performing or underperforming stocks using technical and fundamental indicators.
- **Multi-Timeframe Analysis**: Analyze trends across daily, 4-hour, and 15-minute charts.
- **Real-Time Insights**: Detect market regimes (bullish, bearish, or sideways) and adapt strategies.
- **Sector Analysis**: Track sector performance and correlations between stocks and indices.
- **Interactive Dashboard**: Visualize insights and interact with AI-generated recommendations.
- **Educational Guidance**: Learn trading strategies with mentor-mode explanations and tips.

---

## 🛠️ Installation and Setup

### Prerequisites
1. Install Python (≥ 3.8) and Node.js (≥ 14.x).
2. Obtain API keys from stock data providers (e.g., Alpha Vantage, Yahoo Finance).

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

3. Install Node.js dependencies:
   ```bash
   cd src/dashboard
   npm install
   ```
4. Configure API keys:
   - Copy `config/api_keys_template.json` to `config/api_keys.json`.
   - Add your API keys.

5. Run the backend:
   ```bash
   python src/dashboard/app.py
   ```
6. Start the frontend:
   ```bash
   cd src/dashboard
   npm start
   ```

---

## 💡 Usage
1. Open the dashboard in your browser at `http://localhost:3000`.
2. Use the market scanning feature to identify trading opportunities.
3. Visualize trends and insights through interactive charts and heatmaps.
4. Access AI-generated recommendations tailored to current market conditions.

---

## 🛠️ Data Fetching and Database

### Data Fetching with Yahoo Finance (`yfinance`)
The system uses the `yfinance` library as its primary data provider for stock market data. Note that the data may have a 15-minute delay due to Yahoo Finance's limitations in the free tier.

- **Historical Data**: The script fetches historical stock data using `yfinance` and stores it in a local SQLite database (`tradesman.db`).
- **Schema Setup**: The database includes a `stock_data` table to store fields like `date`, `ticker`, `open`, `close`, `volume`, etc.

### Example Usage
Here’s an example of how to fetch and store data programmatically:
```python
from src.historical_data.historical_data import fetch_and_store_data

# Fetch and store data for Apple stock from 2022 to 2023
fetch_and_store_data("AAPL", "2022-01-01", "2023-01-01")
```

### Simulated Real-Time Updates
To simulate real-time updates (fetching the latest available data periodically):
```python
from src.historical_data.historical_data import simulate_realtime

simulate_realtime("AAPL")
```

---

### Managing the Database File (`tradesman.db`)
- **Location**: The database file is stored locally in the directory where the script is executed.
- **Verification**: Use tools like SQLite CLI, DB Browser for SQLite, or Python scripts to inspect its contents.
- **Recreation**: The file can be recreated by running the script if deleted.

> **Important**: The `tradesman.db` file is not included in the repository to avoid version control issues. You can generate it by running the scripts provided.

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

## 📅 Roadmap
- **Phase 1**: Core features like market scanning, data analysis, and multi-timeframe insights.
- **Phase 2**: Advanced tools such as sector analysis and heatmaps.
- **Phase 3**: Interactive tools like scenario simulations and emotional decision trackers.
- **Phase 4**: Personalization and educational features such as mentor mode.

---

## 📝 Acknowledgments
- Powered by [Alpha Vantage](https://www.alphavantage.co/), [Yahoo Finance](https://finance.yahoo.com/), and other APIs.
- Built with Python, React, and open-source libraries.

---

## 📬 Contact
For questions, feedback, or support, reach out to [Ty-Fonze](https://github.com/Ty-Fonze).
