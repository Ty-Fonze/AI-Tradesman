const { contextBridge } = require('electron');
const path = require('path');

// Import the live ticker module
const liveTicker = require(path.join(__dirname, 'widgets', 'live_ticker'));

// Expose the function to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
  renderLiveTicker: liveTicker.renderLiveTicker,
});
