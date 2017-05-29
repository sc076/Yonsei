'use strict';
module.exports = function(app) {
  var tardy = require('../controllers/tardyController');

  // tardy Routes
  app.route('/')
    .get(tardy.getResponse)
};
