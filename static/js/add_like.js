
$(function () {
$('.like').click(function(){
 alert('Количество лайков = ' + $(this).val());
 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});
 $.ajax({
      url: '/articles/changelike/',
      type: 'post',
      dataType: 'json',
      data: {
        'id': $(this).data('id'),
        'like': $(this).val(),
      },
       success: function(data) {
        alert("Вы кликнули на кнопку и ее значение = ");
        console.log(data);
    }
    });
});
});