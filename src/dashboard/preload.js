const { contextBridge } = require('electron');
const liveTicker = require('./widgets/live_ticker'); // Use relative path

// Expose the liveTicker functionality to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
    renderLiveTicker: liveTicker.renderLiveTicker,
});
