# 📈 AI Tradesman - Your Stock Market Assistant

AI Tradesman is an AI-powered assistant designed to empower traders with smarter decision-making capabilities. By leveraging real-time market data, technical analysis, and advanced AI tools, it provides actionable insights, portfolio management tools, and educational guidance for traders of all levels.

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
