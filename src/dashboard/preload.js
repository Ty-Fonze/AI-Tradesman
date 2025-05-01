const { contextBridge } = require('electron');
const path = require('path');

const liveTicker = require(path.join(__dirname, 'widgets', 'live_ticker'));

contextBridge.exposeInMainWorld('electronAPI', {
  renderLiveTicker: liveTicker.renderLiveTicker
});
