const path = require('path')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  entry: './index.js',
  output: {
    filename: 'app.js',
    path: path.resolve('./')
  },
  devtool: 'cheap-eval-module-map',
  resolve:{
    extensions:['.vue', '.js']
  },
  module:{
    rules:[
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.less$/,
        use: [
          'style-loader',
          'css-loader',
          'less-loader'
        ]
      },
    ]
  },
  plugins:[
    new VueLoaderPlugin()
  ]
}