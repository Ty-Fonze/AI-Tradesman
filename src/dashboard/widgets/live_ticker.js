// Mock ticker data
const mockTickerData = [
  { symbol: 'AAPL', price: 154.12 },
  { symbol: 'GOOGL', price: 2845.23 },
  { symbol: 'AMZN', price: 3456.78 },
  { symbol: 'MSFT', price: 299.45 },
];

// Function to render the Live Ticker Widget
function renderLiveTicker() {
  const tickerContainer = document.createElement('div');
  tickerContainer.className = 'live-ticker';

  // Add each stock ticker to the container
  mockTickerData.forEach((ticker) => {
    const tickerItem = document.createElement('div');
    tickerItem.className = 'ticker-item';
    tickerItem.textContent = `${ticker.symbol}: $${ticker.price.toFixed(2)}`;
    tickerContainer.appendChild(tickerItem);
  });

  return tickerContainer;
}

// Export the widget function
module.exports = { renderLiveTicker };
