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
    $("#priveous").click(function(e) { 
        e.preventDefault();
        $("#home-tab").trigger("click");
        
    });
    $("#accept").click(function (e) { 
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data:
            {   
                "status":"restaurant",
                "name_of_restaurant": $("#r_name").val(),
                "first_name":$("#name").val(),
                "email":$("#email").val(),
                "password":$("#password").val(),
                "repeat_password":$("#r_password").val(),
                "courier":$("#courier").is(":checked"),
                "customer":$("#customer").is(":checked"),
                "employer":$("#employer").is(":checked"),
                "address":document.getElementsByClassName("mapboxgl-ctrl-geocoder--input")[0].value,
                "lng":lng,
                "lat":lat,
            },
            success: function (response) {
                    window.location.href = "/reg/notice";
                
            }
        });
    });
    $('#courier').change(function() {
        if (this.checked){
            if ($('#employer').prop('checked')){
                $("#r_name").css({
                    "display":"none"
                });
                $(".name").css({
                    "top":"20%"
                });
                $(".email").css({
                    "top":"28%"
                });
                $(".password").css({
                    "top":"36%"
                });
                $(".r_password").css({
                    "top":"45%"
                });
                $(".courier").css({
                    "top":"52%"
                });
                $(".customer").css({
                    "top":"56%"
                });
                $(".employer").css({
                    "top":"60%"
                }); 
                $(".btn").css({
                    "top":"64%"
                });
                $('#continue').replaceWith('<button class="btn btn-primary" type="submit" id="reg">Зарегистрироваться</button>');
            }
            $('#employer')[0].checked = false;
            $('#customer')[0].checked = false;
        } 
    });
    $('#customer').change(function() { 
        if (this.checked){
            if($('#employer').prop('checked')){
                $("#r_name").css({
                    "display":"none"
                });
                $(".name").css({
                    "top":"20%"
                });
                $(".email").css({
                    "top":"28%"
                });
                $(".password").css({
                    "top":"36%"
                });
                $(".r_password").css({
                    "top":"45%"
                });
                $(".courier").css({
                    "top":"52%"
                });
                $(".customer").css({
                    "top":"56%"
                });
                $(".employer").css({
                    "top":"60%"
                }); 
                $(".btn").css({
                    "top":"64%"
                });
                $('#continue').replaceWith('<button class="btn btn-primary" type="submit" id="reg">Зарегистрироваться</button>');
            }
            $('#employer')[0].checked = false;
            $('#courier')[0].checked = false;
        }  
    });
    $('#employer').change(function() {
        // this will contain a reference to the checkbox   
        if (this.checked) {
            $('#courier').prop('checked', false);
            $('#customer').prop('checked', false);
            // the checkbox is now checked
            $("#r_name").css({
                "display":"block"
            });
            $(".name").css({
                "top":"28%"
            });
            $(".email").css({
                "top":"36%"
            });
            $(".password").css({
                "top":"44%"
            });
            $(".r_password").css({
                "top":"53%"
            });
            $(".courier").css({
                "top":"60%"
            });
            $(".customer").css({
                "top":"64%"
            });
            $(".employer").css({
                "top":"68%"
            }); 
            $('#reg').replaceWith('<button class="btn btn-primary" type="submit" id="continue">Далее</button>');
            $('#continue').css({
                width: '170px',
                position: 'absolute',
                left:'43%',
                top:'72%',
            });
            $('#continue').click(function(e) {
                e.preventDefault();
                $("#profile-tab").trigger("click");
                $('.mapboxgl-canvas').css({'width':'600px'});
                $('.mapboxgl-canvas').css({'height':'600px'});
                $('#map').css({'width':'600px'});
                $('#map').css({'height':'600px'});
                $("#accept").css({position: "absolute", left:"48%", top:"77%", height: "40px"});
                $("#priveous").css({position: "absolute", left:"30%", top:"77%", height: "40px"});
                if (!map.resized) {
                    map.resized = true
                    window.setTimeout(()=>map.resize(), 500)
                  }
            });
        } 
        else {
            $("#r_name").css({
                "display":"none"
            });
            $(".name").css({
                "top":"20%"
            });
            $(".email").css({
                "top":"28%"
            });
            $(".password").css({
                "top":"36%"
            });
            $(".r_password").css({
                "top":"45%"
            });
            $(".courier").css({
                "top":"52%"
            });
            $(".customer").css({
                "top":"56%"
            });
            $(".employer").css({
                "top":"60%"
            }); 
            $(".btn").css({
                "top":"64%"
            });
            $('#continue').replaceWith('<button class="btn btn-primary" type="submit" id="reg">Зарегистрироваться</button>');
        }
    });


});