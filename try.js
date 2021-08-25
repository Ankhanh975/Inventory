javascript: (function () {
    var speed = prompt("Speed?");
    console.log(speed);
    if (speed != null) {
        document.getElementsByClassName("html5-main-video")[0].playbackRate = speed;
    }
})();
// var link = window.location.href;