$(function () {
$('#btn2').click(function() {
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
        'first-input': $("input[name='first-input']").val(),
        'second-input':  $("input[name='second-input']").val()
      },
       success: function(json) {
       $('.popup-window').fadeIn();
    }
    });
		});
    $('.popup-close').click(function() {
		$(this).parents('.popup-window').fadeOut();
		return false;
	});
    $('.btn3').click(function() {
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
            'name': $("input[name='name']").val(),
            'tag':  $("input[name='tag']").val(),
            'deception':  $("input[name='deception']").val()
          },
           success: function(data) {
           console.log(data);
        }
        });
})
});
