'use strict';
module.exports = function(app) {
  var !tardy = require('../controllers/!tardyController');


  // !tardy Routes
  app.route('/tasks')
    .get(!tardy.list_all_tasks)
    .post(!tardy.create_a_task);


  app.route('/tasks/:taskId')
    .get(!tardy.read_a_task)
    .put(!tardy.update_a_task)
    .delete(!tardy.delete_a_task);
};
