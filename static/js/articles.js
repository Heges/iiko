
$(function () {
 const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

var loadForm = function () {
    var btn = $(this);
    alert('clicled');

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
      beforeSend: function () {
       $("#modal-articles .modal-content").html("");
        $('#modal-articles').show();
      },
      success: function (data) {
        $("#modal-articles .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);

     const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    });
    $.ajax({
      url: '/articles/create/',
      data: form.serialize(),
      type: 'post',
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#articles-table tbody").html(data.html_articles_list);
          $("#modal-articles").modal("hide");
        }
        else {
          $("#modal-articles .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

$(".js-create-articles").click(loadForm);
 $("#modal-articles").on("submit", ".js-articles-create-form", saveForm);

});