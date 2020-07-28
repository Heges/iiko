

$(function () {
$('#minus').click(function(){
 $("#calc-button").val(parseInt($("#calc-button").val())-1),
 alert( $("#calc-button").val());
 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});
 $.ajax({
      url: '/cart/plusValue/',
      type: 'post',
      dataType: 'json',
      data: {
        'id': $(this).data("id"),
        'counts': $("#calc-button").val(),
      },
       success: function(data) {
        alert("Вы кликнули на кнопку и ее значение = "+ data['counts']);
        console.log(data);
    }
    });
});
$('#plus').click(function(){
 $("#calc-button").val(parseInt($("#calc-button").val())+1),
 alert( $("#calc-button").val());
 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});
 $.ajax({
      url: '/cart/plusValue/',
      type: 'post',
      dataType: 'json',
      data: {
        'id': $(this).data("id"),
        'counts': $("#calc-button").val(),
      },
       success: function(data) {
        alert("Вы кликнули на кнопку и ее значение = "+ data['counts']);
        console.log(data);
    }
    });
});
});