import React, { useState, useEffect } from 'react';

function LiveTickerWidget() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Simulate fetching real-time data
    const interval = setInterval(() => {
      setData((prev) => [
        ...prev,
        { symbol: 'AAPL', price: (Math.random() * 1000).toFixed(2) },
      ]);
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ border: '1px solid black', padding: '10px', margin: '10px' }}>
      <h2>Live Ticker</h2>
      <ul>
        {data.map((item, index) => (
          <li key={index}>
            {item.symbol}: ${item.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default LiveTickerWidget;
