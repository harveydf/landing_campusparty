$(function(){

	$('.formulario').on('submit',function(e){
		e.preventDefault();
		var $form = $(this),
			url = $form.attr('action');
			data = $form.serialize();
		$.post(url,data,function(data){
			console.log(data);
			$('.invitacion').text('Gracias por registrarte '+data.name).addClass('finish');
		});
	});
	$('.vermas').on('click',function(e){
		e.preventDefault();
		var $escenario = $(this).parents('.escenario'),
		url            = $(this).attr('href');
		$.get(url,function(data){
			$escenario.addClass('active');
			$escenario.after(data);
		});
	});


});