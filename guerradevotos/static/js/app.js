$(document).ready(function() {
	// Search for registered users
	$('#UserSearchName').keyup(function(){
		$(".loader").show();
		var query;
		query = $(this).val();
		$.get('/users-list/',{userName: query}, function(data){
			$(".users-list").remove();
			$(".no-results").remove();
			$(data).insertAfter('#Users');
			$(".loader").hide();
		});
	});

	$.validator.addMethod('accept', function () { return true; });

    // Upload image
    $("#upload-image-btn").change(function(){
    	var oFReader = new FileReader();
        oFReader.readAsDataURL($(this).prop('files')[0]);
        
        oFReader.onload = function (oFREvent) {
            $("#upload-image").attr("src",oFREvent.target.result);
        };
    });

	// Change controls validation msg
	$.validator.messages.required = 'Este campo es requerido.';
	// Begin duel
	$("#btn-create-duel").on('click', function() {
		$("#CompetitorFrm").validate({
			rules: {
				name: {
					required: true
				},
				description: {
					required: true
				}
			},
			highlight: function(element) {
				$(element).closest('.form-group').removeClass('has-success').addClass('has-error');
			},
			success: function(element) {
				$(element).closest('.form-group').removeClass('has-error').addClass('has-success');
			},
			submitHandler: function(form) {
				$(form).ajaxSubmit({
					dataType: "json",
					url: $(form).attr('action'),
					beforeSubmit: function(){
						$("#btn-create-duel").prop('disabled',true);
						$("#btn-create-duel").html('Espera...');
					},
					success: function(data) {
						if (data.response_id == 1) {	
							hideMessage()
							cleanContent();					
							displayMessage("<span class='alertContent'><strong>Genial!</strong> Tu competidor se registro correctamente. Una solicitud de Duelo ha sido enviada a tu contrincante.</span>", "alert-success");
						} else if (data.response_id == 2) {
							hideMessage();
							displayMessage("<span class='alertContent'><strong>Oh no :( !</strong> Ocurrio un error al guardar el registro, por favor revisa los datos ingresados e intenta de nuevo.</span>", "alert-danger");
						} else if (data.response_id == 3) {
							hideMessage();
							displayMessage("<span class='alertContent'><strong>Oh no :( !</strong> Ocurrio un error al guardar el registro.</span>", "alert-danger");
						}
					}
				});
				$("#btn-create-duel").prop('disabled',false);
				$("#btn-create-duel").html('¡Comience el duelo!');
				return false;
			}
		});
	});

});

// Ajax loaded content, click event handler
$(document).on('click', ".select-opponent", function (e) {
    e.preventDefault();
	var selectedUser = $(this).closest('.users-list');
	$(this).removeClass('btn-primary').addClass('btn-danger');
	$("#UserD").val($(this).attr("data-oppuser"));
	$(".users-list").each(function(){
		$(".users-list").not(selectedUser).remove();
	});
    return false;
});

// Display custom messages
function displayMessage(msg, type) {
	$(".alert").addClass(type).append(msg);
	$(".alert").slideDown(200);
}

// Hide custom messages
function hideMessage() {
	$(".alertContent").remove();
	$(".alert").slideUp(200);
}

// Limpiar variables 
function cleanContent() {
	$("#upload-image").attr("src","http://localhost:8000/static/img/add_image.png");
	$("#upload-image-btn").val('');
	$("#CompetitorName").val('');
	$("#CompetitorDescription").val('');
	$("#UserD").val('');

}

