$(function () {
$('.myInput').click(function() {
    alert('NALAJ')
    $('.popup-open').on('show.bs.modal')
});

$('.popup-close').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});
});
