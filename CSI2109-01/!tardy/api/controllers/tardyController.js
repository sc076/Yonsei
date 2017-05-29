'use strict';

//If database is needed
var mongoose = require('mongoose'),
  Task = mongoose.model('Tasks');

// here is a message send to the page
exports.getResponse = function(req, res) {
  res.json({ message: 'Here goes response' });
};
