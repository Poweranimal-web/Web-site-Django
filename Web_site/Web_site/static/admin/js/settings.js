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
    $(".nav-link8").css({
      color: "black",
      "background-color": "transparent",
      "font-size":"small",
      width:"256px",  
      height:"32px",
      "text-align":"start",
      border:"0.1px gray solid",
      "margin-bottom": "5px"
    });
    $(".f").css({
      position: "absolute",
      left: "14%",
      top: "28%",
      "width":"200px"

    })
    $(".nav-link8").hover(function(){
      if ($(this).attr("class")!="nav-link8 active"){
      $(this).css({
        "background-color": "rgb(192,192,192)",
      });
    }
      else{
        $(this).css({
          "background-color": "rgb(128,128,128)",
        });
      }
    },
    function(){
      if ($(this).attr("class")!="nav-link8 active"){
      $(this).css({
        "background-color": "transparent",
      });
    }
      else{

      }
    });
    $(".nav-link8").click(function (e) { 
      $(this).css({
        "background-color": "rgb(128,128,128)",
      });
      $(this).siblings(".nav-link8").css({
        "background-color": "transparent",
      });
      
    });
    $("#v-pills-profile-tab").trigger("click");
    $(".devider").css({
      width: "800px",
      "margin-top": "0"

    })
    $("#v-pills-profile").css({
      position: "relative",
      left:"20%",
    });
    $(".Subhead-heading").css({
      "font-size": "20px",
      "font-weight": "400",
    });
    $("#update").css({
      "color":"white",
      "background-color":"#2da44e",
      position: "absolute",
      top:"155%"
    });
    $("#delete_heading").css({
      position:"absolute",
      top:"190%",
      "font-weight": "600",
      "color": "#cf222e"

    });
    $("#delete_devider").css({
      position:"absolute",
      top:"210%"
    });
    $("#warning").css({
      position:"absolute",
      top:"220%",
    });
    $("#delete_ac").css({
      position:"absolute",
      top:"240%",
      "background-color":"gainsboro",
      "color":"red",
    });
    $("#delete_ac").hover(
      function(){
        $(this).css({
          "background-color":"red",
          "color":"gainsboro",
        });
      },
      function(){
        $(this).css({
          "background-color":"gainsboro",
          "color":"red",
        });
      }

    );
    $("#update").hover(
      function(){
        $(this).css({
          "background-color":"#24833e",
        });
      },
      function(){
        $(this).css({
          "background-color":"#2da44e"
        });
      }

    );
    $("#update_data").submit(function (e) { 
      e.preventDefault();
      $.ajax({
        type: "POST",
        url: window.location.pathname,
        data: $(this).serialize(),
        success: function (response) {
          alert("updated");
        }
      });
    });
    $("#delete_ac").click(function (e) { 
      e.preventDefault();
      $.ajax({
        type: "DELETE",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({"set":"delete_account"}),
        url: window.location.pathname,
        dataType: 'text',
        success: function (response) {
          window.location.pathname = '/'
        }
      });
    });

});