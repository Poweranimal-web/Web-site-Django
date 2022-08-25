function getCSRFToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCSRFToken("csrftoken") }
    });
    $("#accept").click(function (e) { 
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
            "address":document.getElementsByClassName("mapboxgl-ctrl-geocoder--input")[0].value,
            lng:"",
            ltg:""
            },
            success: function (response) {
                
            }
        });
        console.log(document.getElementsByClassName("mapboxgl-ctrl-geocoder--input")[0].value);
    });    


});