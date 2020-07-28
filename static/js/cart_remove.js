
$(function () {
  $(".js-take-cart-id-delete").click(function () {
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});
    $.ajax({
      url: '/cart/',
      type: 'post',
      dataType: 'json',
      data: {
        'id': $(this).data("id"),
      },
       success: function(data) {
        alert("Вы удавили из корзину позицию = "+ data['name']);
        console.log(data);
    }
    });
  });
});