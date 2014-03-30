$( document ).ready(function() {
	$('#UserSearchName').keyup(function(){
		$(".loader").show();
		var query;
		query = $(this).val();
		$.get('/users-list/',{userName: query}, function(data){
			$(".users-list").remove();
			$("#btn-create-duel").remove();
			$(".no-results").remove();
			$(data).insertAfter('#Users');
			$(".loader").hide();
		});
	});
});
