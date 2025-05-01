import time
import schedule
from real_time_stock import fetch_and_store_realtime_data
from alerts import check_alerts

# Define stock symbols and thresholds
symbols = [
    {"symbol": "AAPL", "threshold": 175},
    {"symbol": "MSFT", "threshold": 320},
]

# Job to fetch data and check alerts
def job():
    for item in symbols:
        fetch_and_store_realtime_data(item["symbol"])
        check_alerts(item["symbol"], item["threshold"])

# Schedule the job
schedule.every(1).minutes.do(job)

if __name__ == "__main__":
    print("Starting real-time stock monitoring...")
    while True:
        schedule.run_pending()
        time.sleep(1)
