var main = function () {
	'user strict'
	var $result,
		page;

	$("#filter").click(function() {
		if($("#filtertext").val() === "") {
			alert("Enter a valid input");
			$("#filtertext").val('');
		}
		else{
			page = $("#filtertext").val() + '.html';
			window.location = page;
		}
	});

	$('#filtertext').keyup(function(event){
		if(event.keyCode == 13){
			console.log("enter worked");
			$("#filter").click();
		}
	});	

}
$(document).ready(main);