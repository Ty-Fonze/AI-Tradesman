const path = require('path');

mainWindow = new BrowserWindow({
  width: 1200,
  height: 800,
  webPreferences: {
    preload: path.join(__dirname, 'preload.js'), // Ensure this is correct
    contextIsolation: true,
    enableRemoteModule: false,
    nodeIntegration: false,
  },
});
