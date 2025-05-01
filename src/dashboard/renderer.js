const { renderLiveTicker } = require('./widgets/live_ticker');

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('app');

    // Add the Live Market Ticker Widget to the dashboard
    const liveTickerWidget = renderLiveTicker();
    appContainer.appendChild(liveTickerWidget);
});
