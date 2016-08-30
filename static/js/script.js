

$('.message a').click(function() {
    $('form').animate({ height: "toggle", opacity: "toggle" }, "slow");
});

function signup() {
    console.log("signup clicked");
    $("#pagetwo").click();

}

function login() {
    console.log("login clicked");
    $("#pagetwo").click();
}

function hasGetUserMedia() {
    return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia || navigator.msGetUserMedia);
}

