'use strict';
module.exports = function(app) {

  var path = require('path');

  app.get('/', function(req, res) {
    res.render(path.join(__dirname+'/../views/index'));
    //__dirname : It will resolve to your project folder.
  });
};
