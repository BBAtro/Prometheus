const { resolve } = require('path');
 
module.exports = {
  root: resolve('./frontend/src'),
  base: '/frontend/',
  server: {
    host: '0.0.0.0',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json'],
  },
  build: {
    outDir: resolve('./frontend/dist'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./frontend/src/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};