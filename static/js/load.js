$(function () {
  $(".js-create-articles").click(function () {
  $.post( "/cart", { name: "John", time: "2pm" })
        .done(function( data ) {
         alert( "Data Loaded: " + data );
  });
  });
});