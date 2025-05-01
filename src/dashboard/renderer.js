document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('app');

    // Add the Live Market Ticker Widget to the dashboard
    const liveTickerWidget = window.electronAPI.renderLiveTicker();
    appContainer.appendChild(liveTickerWidget);
});
