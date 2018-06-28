// mysql_utilities module takes care of DB related operations
var mysql_utilities = require('./mysql_utilities');
// mail_handler is used for sending email to recipients
var mail_handler = require('./mail_handler');

exports.store_user_name = function(request,response){
  var contents = request.body;
  var first_name = contents.first_name;
  var last_name = contents.last_name;
  mysql_utilities.insert_data(first_name,last_name,response);
};

exports.get_last_name = function(req,res){
  var first_name = req.query.first_name;
  mysql_utilities.select_data(first_name,res);
};

exports.send_email_to_recipients = function(req,res){
  var contents = req.body;
  var to = contents.to;
  var subject = contents.subject;
  var body = contents.body;
  mail_handler.send_email_to_recipients(to,subject,body);
  res.send('Email sent successfully');
}
