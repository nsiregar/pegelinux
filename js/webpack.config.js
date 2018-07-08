const path = require('path');

module.exports = {
  entry: [
    './src/application.js',
  ],

  output: {
    filename: 'application.js',
    path: path.resolve(__dirname, '../app/assets/js')
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015']
        }
      }
    ]
  }
};
