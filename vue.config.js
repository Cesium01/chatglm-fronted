const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    proxy: {
      '/chat': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/chat': '/'
        }
      }
    }
  }
}
