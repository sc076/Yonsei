var express = require('express'),
  app = express(),
  port = process.env.PORT || 8000,
  mongoose = require('mongoose'),
  Task = require('./api/models/!tardy'),
  bodyParser = require('body-parser');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/Tardydb');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var routes = require('./api/routes/!tardy');
routes(app);

app.set('view engine', 'pug');
app.get('/', function(req, res) {
  res.render('template/template', {title: 'Hey', message: 'Hello World!'});
})

app.listen(port);

console.log('!TARDY RESTful API server started on: ' + port);

app.use(function(req, res) {
  res.status(404).send({url: req.originalUrl + ' not found'})
});
