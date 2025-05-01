const { contextBridge } = require('electron');

// Expose an API to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
  require: (module) => require(module), // Exposes `require` to the renderer
});
