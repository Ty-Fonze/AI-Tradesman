const { renderLiveTicker } = require('./widgets/live_ticker');

document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('app');

    // Add the Live Market Ticker Widget to the dashboard
    const liveTickerWidget = renderLiveTicker();
    appContainer.appendChild(liveTickerWidget);
});
