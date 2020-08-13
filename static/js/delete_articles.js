$(function () {
$('.button-delete').click(function() {
		 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
         $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
});
 $.ajax({
      url: '/articles/' + $(this).data('id') + '/',
      type: 'post',
      dataType: 'data',
      data: {
        'key': 'remove',
        'id': $(this).data('id'),
      },
       success: function(data) {
       alert('yra');
       $("#articles-table #tbody").html(data['html_form_detail']);
    }
    });
		});
});
