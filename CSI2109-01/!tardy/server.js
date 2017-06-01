var express = require('express'),
  app = express(),
  path = require('path'),
  port = process.env.PORT || 8000,
  mongoose = require('mongoose'),
  Task = require('./api/models/tardyModel'),
  bodyParser = require('body-parser');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/Taskdb');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());


var routes = require('./api/routes/tardyRoutes');
routes(app);

// view engine setup
app.set('view engine', 'pug');
app.set('views', './api/views');

app.use(express.static('./api/views'));

app.listen(port);

console.log('!TARDY RESTful API server started on: ' + port);

app.use(function(req, res) {
  res.status(404).send({url: req.originalUrl + ' not found'})
});
