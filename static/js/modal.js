$(function () {
$('.popup-open').click(function() {
        var contactHTML = $('.p').text();
        console.log(contactHTML);
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
       success: function(json) {
       $('.popup-fade').fadeIn();
        $('.p').text(json['infa']);
        console.log(json['infa']);
    }
    });
		});
$('.popup-close').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});
});
