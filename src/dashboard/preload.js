const { contextBridge } = require('electron');

// Expose 'require' to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
    require: (module) => require(module),
});
