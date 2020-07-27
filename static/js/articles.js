
$(function () {
  $(".js-create-articles").click(function () {
    $.ajax({
      url: '/articles/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-articles").modal("show");
      },
      success: function (data) {
        $("#modal-articles .modal-content").html(data.html_form);
      }
    });
  });

});