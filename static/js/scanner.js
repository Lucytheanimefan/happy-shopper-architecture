'use strict';

//spinner
var opts = {
    lines: 13 // The number of lines to draw
        ,
    length: 28 // The length of each line
        ,
    width: 14 // The line thickness
        ,
    radius: 42 // The radius of the inner circle
        ,
    scale: 1 // Scales overall size of the spinner
        ,
    corners: 1 // Corner roundness (0..1)
        ,
    color: '#000' // #rgb or #rrggbb or array of colors
        ,
    opacity: 0.25 // Opacity of the lines
        ,
    rotate: 0 // The rotation offset
        ,
    direction: 1 // 1: clockwise, -1: counterclockwise
        ,
    speed: 1 // Rounds per second
        ,
    trail: 60 // Afterglow percentage
        ,
    fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
        ,
    zIndex: 2e9 // The z-index (defaults to 2000000000)
        ,
    className: 'spinner' // The CSS class to assign to the spinner
        ,
    top: '50%' // Top position relative to parent
        ,
    left: '50%' // Left position relative to parent
        ,
    shadow: false // Whether to render a shadow
        ,
    hwaccel: false // Whether to use hardware acceleration
        ,
    position: 'absolute' // Element positioning
}

var videoElement = document.querySelector('video');

var videoSelect = document.querySelector('select#videoSource');

navigator.getUserMedia = navigator.getUserMedia ||
    navigator.webkitGetUserMedia || navigator.mozGetUserMedia;

function gotSources(sourceInfos) {
    for (var i = 0; i !== sourceInfos.length; ++i) {
        var sourceInfo = sourceInfos[i];
        var option = document.createElement('option');
        option.value = sourceInfo.id;
        if (sourceInfo.kind === 'video') {
            option.text = sourceInfo.label || 'camera ' + (videoSelect.length + 1);
            videoSelect.appendChild(option);
        } else {
            console.log('Some other kind of source: ', sourceInfo);
        }
    }
}

if (typeof MediaStreamTrack === 'undefined' ||
    typeof MediaStreamTrack.getSources === 'undefined') {
    alert('This browser does not support MediaStreamTrack.\n\nTry Chrome.');
} else {
    MediaStreamTrack.getSources(gotSources);
}

function successCallback(stream) {
    window.stream = stream; // make stream available to console
    videoElement.src = window.URL.createObjectURL(stream);
    videoElement.play();
}

function errorCallback(error) {
    console.log('navigator.getUserMedia error: ', error);
}

function start() {
    if (window.stream) {
        videoElement.src = null;
        window.stream.stop();
    }

    var videoSource = videoSelect.value;
    var constraints = {
        video: {
            optional: [{
                sourceId: videoSource
            }]
        }
    };
    navigator.getUserMedia(constraints, successCallback, errorCallback);
}


videoSelect.onchange = start;

start();

// Grab elements, create settings, etc.
var mainContent = document.getElementById("visuals");
var video = document.getElementById('video');
var canvas = document.createElement("canvas");
canvas.setAttribute("width", "640px");
canvas.setAttribute("height", "480px");
canvas.id = "canvas";

var proceedButton = document.createElement("button");
proceedButton.id = "proceed";
proceedButton.innerHTML = "Proceed";

//var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
// Get access to the camera!

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
    console.log("Clicked snap!");
    mainContent.appendChild(canvas);
    context.drawImage(video, 0, 0, 640, 480);
    $("#video").hide();

    //start spinner
    var target = document.getElementById('spinner');
    var spinner = new Spinner(opts).spin(target);
    console.log("Spinner going");

    setTimeout(function(){
      document.getElementById("checkout").click();
    },2000);
});
