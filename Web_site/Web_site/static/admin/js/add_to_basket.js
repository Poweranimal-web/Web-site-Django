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
function getCookies(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
$(document).ready(function () {
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCSRFToken("csrftoken") }
        });
        $(".star").css({
          "font-size": "45px",
          "color": "red",
          "position": "absolute",
          "top": "-418px",
          "left": "355px",
        });
        $(".star").rate();
        $(".star").click(function(e){
            e.preventDefault();
            $.ajax({
              type: "POST",
              url: window.location.pathname,
              data: {
                "status":"add_rating",
                "rating": $(this).rate("getValue"),
              },
              success: function (response) {
                
              }
            });
        });
        $("#dish-tab").trigger("click");
        $('#num').html(getCookies("number_meal_basket"));
        $('#num').css({position: "absolute",
                       bottom: "3.5%",
                       left: "67.5%",
                       "font-weight": "800",
        });
        $("#basket").css({width:"90px",
                          height:"57px",
        });
        $('.brt').click(function (e) { 
            e.preventDefault();
            $.ajax({
                method: "POST",
                url: window.location.pathname,
                data: {"IN":$(this).val(),
                       "auth": getCookies("auth"),
                       "status": "add_product"
                },
                success: function(){ 
                        var auth_check = getCookies("auth");
                        if(String(auth_check) == null || String(auth_check) == "False"){
                          window.location.href = "/auth/";
                        }
                        else {
                          $('#num').html(getCookies("number_meal_basket"));
                          console.log("Nice");
                        }
                      }
            });
        });
    });
