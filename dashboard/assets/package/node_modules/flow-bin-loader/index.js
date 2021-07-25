const spawn = require('child_process').spawn;

module.exports = function(source, map) {
  const cb = this.async();
  const flow = spawn(require('flow-bin'), ['check-contents']);

  let stdout = '';
  flow.stdout.on('data', (data) => {
    stdout += data;
  });

  flow.on('close', (code) => {
    if(code)
      console.log(stdout.replace(/^-(:[0-9]+.*)/, `${this.resourcePath}$1`));

    cb(code ? code : null, source, map);
  });

  flow.stdin.write(source)
  flow.stdin.end();
};
