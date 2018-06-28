var email_form = $('#email_form');
var send_email_url = '/send_email_to_recipients';
email_form.submit(function(){
  event.preventDefault();
  var formData = email_form.serialize();
  $.ajax({
    url: send_email_url,
    dataType: "text",
    type: "POST",
    data: formData,
    success: function(result){
      window.alert(result);
      email_form.trigger('reset');
    },
    error : function(result){
       window.alert("Internal Server Error");
    }
  });
});
