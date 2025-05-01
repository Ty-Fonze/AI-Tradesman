# Redis Real-Time Stock Monitoring

This module fetches real-time stock data, stores it in Redis, and raises alerts if specified thresholds are exceeded.

## How It Works
1. **Fetch Stock Data**: Uses `yfinance` to retrieve minute-by-minute stock data.
2. **Store in Redis**: Stores the latest stock data with a time-to-live (TTL) of 60 seconds.
3. **Alerts**: Checks if stock price exceeds predefined thresholds and triggers alerts.

## Files
- `redis_connection.py`: Handles Redis connection.
- `real_time_stock.py`: Fetches and stores stock data in Redis.
- `get_stock_data.py`: Retrieves data from Redis.
- `alerts.py`: Checks for alerts based on thresholds.
- `main.py`: Combines everything and schedules periodic updates.
- `requirements.txt`: Dependencies for the module.

## Running the Module
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the script:
   ```bash
   python main.py
   ```

## Customization
- Add or modify stock symbols and thresholds in `main.py`.
- Adjust Redis settings in `redis_connection.py`.
