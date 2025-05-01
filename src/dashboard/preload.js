const { contextBridge } = require('electron');
const path = require('path');

// Load the live_ticker module
const liveTicker = require(path.join(__dirname, 'widgets/live_ticker'));

// Expose the liveTicker functionality to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
    renderLiveTicker: liveTicker.renderLiveTicker,
});
