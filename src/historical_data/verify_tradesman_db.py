import sqlite3

DATABASE_FILE = "tradesman.db"

def verify_data():
    # Connect to the SQLite database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Query the data
    cursor.execute("SELECT * FROM stock_data WHERE ticker = 'AAPL';")
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    verify_data()