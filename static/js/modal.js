$(function () {
$('.popup-open').click(function() {
		 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
         $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
});
 $.ajax({
      url: '/articles/create/',
      type: 'post',
      dataType: 'json',
      data: {
        'key': 'remove',
        'id': $(this).data('id'),
      },
       success: function(json) {
       $('.popup-fade').fadeIn();
    }
    });
		});
$('.popup-close').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});
});
