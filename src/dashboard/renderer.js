document.addEventListener('DOMContentLoaded', () => {
  const appContainer = document.getElementById('app');

  // Check that electronAPI is defined
  if (window.electronAPI && typeof window.electronAPI.renderLiveTicker === 'function') {
    const liveTickerWidget = window.electronAPI.renderLiveTicker();
    appContainer.appendChild(liveTickerWidget);
  } else {
    console.error('renderLiveTicker is not defined on window.electronAPI');
  }
});
