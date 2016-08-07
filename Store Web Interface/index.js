var express = require('express');

var app = express();

// Create our Express router
var router = express.Router();

// Initial dummy route for testing
router.get('/', function(req, res) {
  res.end('Twitatron');
});

// Register all our routes
app.use(router);

// Start the server
app.listen(3000);