const { contextBridge } = require('electron');
const path = require('path');

// Expose an API to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
  require: (module) => require(module),
  pathJoin: (...args) => path.join(...args),
});
