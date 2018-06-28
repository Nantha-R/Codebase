// Module for sending mails
var nodemailer = require('nodemailer');

function get_transporter()
{
  // Function used for initializing the transporter object
  var transporter = nodemailer.createTransport({
    service: 'gmail',
    tls:
    {
      rejectUnauthorized: false
    },
    auth:
    {
      user: 'sender@gmail.com',
      pass: 'password'
    }
  });
  return transporter;
}

function get_mail_contents(to,subject,body)
{
  // Function used for composing mail contents
  var mail_contents = {
    from: 'sender@gmail.com',
    to: to,
    subject: subject,
    text: body
  };
  return mail_contents;
}

function send_email(transporter,mail_contents)
{
  // Function used for sending mail
  transporter.sendMail(mail_contents, function(error, info){
    if (error)
    {
      console.log(error);
    }
  });
}

exports.send_email_to_recipients = function(to,subject,body){
  var transporter = get_transporter();
  var mail_contents = get_mail_contents(to,subject,body);
  send_email(transporter,mail_contents);
};
