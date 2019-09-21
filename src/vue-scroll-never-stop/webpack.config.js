const path = require('path')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  entry: './index.js',
  output: {
    filename: 'app.js',
    path: path.resolve('./')
  },
  resolve:{
    extensions:['.vue', '.js']
  },
  module:{
    rules:[
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
    ]
  },
  plugins:[
    new VueLoaderPlugin()
  ]
}