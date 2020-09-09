 var modal = document.getElementById("call");
 var btn = document.getElementById("call-call");
 var span = document.getElementsByClassName("close-call")[0];

 btn.onclick = function () {
    call.style.display = "block";
 }

 span.onclick = function () {
    call.style.display = "none";
 }

 window.onclick = function (event) {
    if (event.target == modal) {
        call.style.display = "none";
    }
}