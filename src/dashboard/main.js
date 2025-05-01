const path = require('path');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Correct path to preload.js
      contextIsolation: true, // Security feature
      enableRemoteModule: false, // Deprecated, should be false
      nodeIntegration: false, // Keep disabled for security
    },
  });

  mainWindow.loadFile('index.html');
});
