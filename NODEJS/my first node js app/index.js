// Used for express js framework
var express = require('express');
var app = express();

// manage_data module is used for managing the user request
var manage_data = require('./manage_data');

// Used for parsing the post parameters.
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

// Used to include static files
app.use(express.static('public'))

// Template engine for node js
app.set('view engine', 'ejs');

app.get('/index', function (req, res) {
  console.log("Serving file index.html");
  res.sendFile(__dirname + "/htmlFiles/index.html" );
})

app.get('/put_input_data',function(req,res){
  console.log("Serving file input_data.html");
  res.sendFile(__dirname + '/htmlFiles/input_data.html');
})

app.get('/get_input_data',function(req,res){
  console.log("Serving file get_data.html");
  res.sendFile(__dirname + '/htmlFiles/get_data.html');
})

app.get('/compose_email',function(req,res){
  console.log("Serving file send_email.html");
  res.sendFile(__dirname + '/htmlFiles/compose_email.html');
})

app.post('/store_user_name',urlencodedParser,function(req,res){
  // Storing the name of the user
  manage_data.store_user_name(req,res);
})

app.get('/display_last_name',function(req,res){
  // Retrieving the Last name of the user
  manage_data.get_last_name(req,res);
})

app.post('/send_email_to_recipients',urlencodedParser,function(req,res){
  // Sending emails to recipient
  manage_data.send_email_to_recipients(req,res);
})

// Server starts and listens to port address 8080
var server = app.listen(8080, function () {
   console.log("Starts listening at port 8080");
})
