# 📈 AI Tradesman - Your Stock Market Assistant

AI Tradesman is an AI-powered assistant designed to empower traders with smarter decision-making capabilities. By leveraging real-time market data, technical analysis, and advanced AI tools, it provides actionable insights and a streamlined trading experience.

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

## 🛠️ Current Progress
### Backend
- **AI Integration**: Backend AI is functional and ready for integration with the frontend.
- **Real-Time Monitoring**: Redis-based system fetches live stock data and triggers alerts based on predefined thresholds.
- **Data Handling**:
  - Historical stock data is stored in a local SQLite database.
  - Real-time stock data is stored in Redis for fast access and periodic updates.
- **APIs**: Flask-SocketIO is set up for real-time communication between the backend and frontend.

### Frontend
- **React Dashboard**:
  - The base dashboard is implemented using React and Electron.
  - Widgets like `LiveTickerWidget` are functional and display dynamic content.
- **Planned Enhancements**:
  - Movable and scalable widgets using libraries like `react-grid-layout`.
  - A central widget to serve as the "host dashboard."
  - AI backend integration for dynamic widget interaction.

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
The Redis-based real-time monitoring module fetches live stock data, stores it in Redis, and triggers alerts based on thresholds.

1. Start the monitoring script:
   ```bash
   python src/realtime_data/main.py
   ```
   
2. Check for alerts:
   - Alerts will be printed to the console if a stock price exceeds a threshold.
   - Example:
     ```plaintext
     🚨 Alert: AAPL price is above 175 -> 176.5
     ```

3. Verify Redis storage:
   - Use `redis-cli` to inspect stored data:
     ```bash
     redis-cli
     keys *
     ```

---

## ⚙️ Planned Enhancements
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
[ Market APIs ]            [ News APIs ]            [ Product Docs ]
       |                        |                         |
       +------------------------+-------------------------+
                                |
                         [ Unified API Layer ]
                        /     |      |      \
                [Portfolio] [Alerts] [News] [Education/Help]
                        \     |      |      /
                         [ Event/Notification Bus ]
                                |
                        [ Context Aggregator ]
                                |
             +------------------+-------------------+
             |                                      |
    [React/Electron UI]                   [AI Assistant Service]
             |                                      |
           [User]                                 [User]

## 📬 Contact
For questions, feedback, or support, reach out to [Ty-Fonze](https://github.com/Ty-Fonze).
