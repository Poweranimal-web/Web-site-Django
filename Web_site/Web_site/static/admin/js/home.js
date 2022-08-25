function getCookie(name) {
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
$(document).ready(function(){
$.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
});
$('#num').html(getCookie("number_meal_basket"));
$('#num').css({position: "absolute",
                bottom: "3.5%",
                left: "67.5%",
                "font-weight": "800",
});
$("#basket").css({width:"90px",
                  height:"57px",
});
$("#sign_out").click(function(e){
    e.preventDefault();    
    $.ajax({
            type: "DELETE",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({"set":"sign_out"}),
            url: window.location.pathname,
            dataType: 'text',
            success: function (response) {
                window.location.reload();
            }
        })
    });    
});
