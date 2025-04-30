CREATE TABLE IF NOT EXISTS historical_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date DATE NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    adj_close REAL,  -- Ensure this column exists
    volume INTEGER,
    UNIQUE(symbol, date)
);

CREATE INDEX IF NOT EXISTS idx_symbol_date ON historical_data (symbol, date);
