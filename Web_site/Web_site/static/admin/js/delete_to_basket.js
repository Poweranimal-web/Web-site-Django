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
$(document).ready(function(){
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCSRFToken("csrftoken") }
    });
    $(".number").css({
        position: "absolute",
        right: "9%",
        bottom: "23%",
    });
    $('.plus').css({
        position: "relative",
        width:"36px",
        left:"75%",
        
    });
    $('.minus').css({
        position: "relative",
        width:"36px",
        left:"85%",
    });
    $(".img-fluid").css({
        "width": "285px",
        "height":"217px",
    });
    $(".minus").click(function(e){
        e.preventDefault();
        var allValues = $(this).val();
        var values = JSON.parse(allValues);
        var data = values[0];
        // console.log(data);
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {"IN":data["IN"],
                   "status": "reduce"
            },
            success: $.proxy(function (response) {
                if (Number(data["num"])-1<=0){
                    $(this).siblings(".number").text(0);
                    let new_price =Number(data["price"])*(0);
                    $(this).siblings(".price").text(new_price+" ");
                    console.log($(this).siblings(".number").text());
                    // setCookie("number_meal_basket",0,1);
                }
                else{
                    setCookie("number_meal_basket",Number(getCookies("number_meal_basket"))-1,1);
                    $(this).siblings(".number").text(Number($(this).siblings(".number").text())-1);
                    let new_price =Number(data["price"])*(Number($(this).siblings(".number").text()));
                    $(this).siblings(".price").text(new_price+" "+data["currency"]);
                    var r = /\d+/;
                    $("#total").text("Товары на сумму:"+" "+(Number(($("#total").text()).match(r))-Number(data["price"]))+" "+"UA");
                } 
            },this)
        });
    });
    $(".plus").click(function(e){
        e.preventDefault();
        var allValues = $(this).val();
        var values = JSON.parse(allValues);
        var data = values[0];
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {"IN":data["IN"],
                   "status": "increase"
            },
            success: $.proxy(function (response) {
                setCookie("number_meal_basket",Number(getCookies("number_meal_basket"))+1,1);
                $(this).siblings(".number").text(Number($(this).siblings(".number").text())+1);
                let new_price =Number(data["price"])*(Number($(this).siblings(".number").text()));
                $(this).siblings(".price").text(new_price+" "+data["currency"]);
                var r = /\d+/;
                $("#total").text("Товары на сумму:"+" "+(Number(($("#total").text()).match(r))+Number(data["price"]))+" "+"UA");

            },this)
        });
    });
    $(".btn-close").click(function(e){
        e.preventDefault();
        $.ajax({
            type: "DELETE",
            url: window.location.pathname,
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({"IN":$(this).val()}),
            dataType: 'text',
            success: $.proxy(function (response) {
                if (Number(getCookies("number_meal_basket"))-1<=0){
                    setCookie("number_meal_basket",0,1);
                }
                else{setCookie("number_meal_basket",Number(getCookies("number_meal_basket"))-Number($(this).siblings(".number").text()),1);}
                $(this).parents().parents().parents().parents().parents(".column").remove();
                var r = /\d+/;
                $("#total").text("Товары на сумму:"+" "+(Number($("#total").text().match(r))-Number($(this).siblings(".price").text().match(r)))+" "+"UA");
            },this)
        });
    });
    $("#accept").click(function(e){
        var r = /\d+/;
        setCookie("amount",Number($("#total").text().match(r)),1);       
    }
    ); 
    $("#priveous").click(function(e) { 
        e.preventDefault();
        $("#home-tab").trigger("click");
        
    });
    $("#pay").click(function (e) { 
        e.preventDefault();
        $("#profile-tab").trigger("click");
        $('.mapboxgl-canvas').css({'width':'600px'});
        $('.mapboxgl-canvas').css({'height':'600px'});
        $('#map').css({'width':'600px'});
        $('#map').css({'height':'600px'});
        $("#accept").css({position: "absolute", left:"50.5%", top:"77%", height: "40px"});
        $("#priveous").css({position: "absolute", left:"30%", top:"77%", height: "40px"});
        if (!map.resized) {
            map.resized = true
            window.setTimeout(()=>map.resize(), 500)
        }
        
    });
});