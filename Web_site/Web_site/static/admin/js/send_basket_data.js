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
$(document).ready(function () {
    var form = $("#Profileform");
    // console.log(form);
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $("#logo").css({
        width: "400px",
        height: "400px",
        position:"absolute", 
        left:"60%",
    })
    $("#Profileform").submit(function (e) { 
        e.preventDefault();
        console.log($(this).serializeArray()); 
        var form = new FormData($(this)[0]);  
        $.ajax({
            method: "POST",
            url: "/e_admin/profile/",
            data: form,
            processData: false,
            contentType: false,
            success: $("#close").trigger("click")
        });
        
    });    
});