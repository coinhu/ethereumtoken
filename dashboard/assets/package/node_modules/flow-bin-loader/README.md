# flow-bin-loader

[![npm version](https://badge.fury.io/js/flow-bin-loader.svg)](http://badge.fury.io/js/flow-bin-loader)

A [webpack](https://webpack.github.io/) loader built around
[flow-bin](https://www.npmjs.com/package/flow-bin)
to enforce type checking with [Flow](https://flowtype.org/).

## Installation

```{.sh}
$ npm install --save-dev flow-bin flow-bin-loader
```

## Usage

Add the plugin to your webpack config as follows:

```javascript
module: {
  rules: [
    {
      test: /\.jsx?$/,
      loader: 'flow-bin-loader',
      exclude: /node_modules/,
      enforce: 'pre',
    }
  ]
},
```

Don't forget to add `// @flow` to the top of the files you want to be checked.

## Configuration

By default, modules are resolved with respect to the directory where
`.flowconfig` lives, so you might need to tell Flow how to map paths to the
correct directory.

In order to do that, create a file named `.flowconfig` in the root directory
of your project and add a module mapper rule such as the one below.

```
[options]
module.name_mapper='^\(.*\)$' -> '<PROJECT_ROOT>/src/\1'
```

For the complete list of options, visit
https://flowtype.org/docs/advanced-configuration.html
