$(document).ready(function() {
	// Search for registered users
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
				$.ajax({
					data: $(form).serialize(),
					type: $(form).attr('method'),
					dataType: "json",
					url: $(form).attr('action'),
					success: function(data) {
						if (data.codigo == 1) {
							bloquearControles(form, false);
							mostrarMensaje(form, "<span class='alertContent'><strong>Genial!</strong> El registro se guardo correctamente.</span>", "alert-success");
						} else if (data.codigo == 2) {
							mostrarMensaje(form, "<span class='alertContent'><strong>Oh no :( !</strong> Ocurrio un error al guardar el registro, por favor comunicate con el administrador.</span>", "alert-danger");
						} else if (data.codigo == 3) {
							mostrarMensaje(form, "<span class='alertContent'><strong>Alto!</strong> ERROR, Acta duplicada.</span>", "alert-danger");
						}
					}
				});
				return false;
			}
		});
	});

	

});

// Ajax loaded content, click event handler
$(document).on('click', ".select-opponent", function (e) {
    e.preventDefault();
	var selectedUser = $(this).closest('.users-list');
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

