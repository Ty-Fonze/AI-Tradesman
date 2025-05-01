const renderLiveTicker = window.electronAPI.require('./widgets/live_ticker').renderLiveTicker;

document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('app');

    // Add the Live Market Ticker Widget to the dashboard
    const liveTickerWidget = renderLiveTicker();
    appContainer.appendChild(liveTickerWidget);
});
