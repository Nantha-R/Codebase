var input_form = $('#input_form');
var input_data_url = '/store_user_name';
input_form.submit(function(){
  event.preventDefault();
  var formData = input_form.serialize();
  $.ajax({
    url: input_data_url,
    dataType: "text",
    type: "POST",
    data: formData,
    success: function(result){
      window.alert(result);
      input_form.trigger('reset');
    },
    error : function(result){
       window.alert("Internal Server Error");
    }
  });
});
