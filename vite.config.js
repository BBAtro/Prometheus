const { resolve } = require('path');
 
module.exports = {
  root: resolve('./book_depository/static/src'),
  base: '/book_depository/static/',
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
    outDir: resolve('./book_depository/static/dist'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./book_depository/static/src/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};