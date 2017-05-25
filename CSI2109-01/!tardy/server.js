var express = require('express'),
  app = express(),
  port = process.env.PORT || 8000;

app.listen(port);

console.log('!TARDY RESTful API server started on: ' + port);
