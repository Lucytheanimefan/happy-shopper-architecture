$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

function signup(){
	console.log("signup clicked");
	$("#pagetwo").click();

}

function login(){
	console.log("login clicked");
	$("#pagetwo").click();
}