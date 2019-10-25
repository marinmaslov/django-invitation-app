function createNewInvitation() {
    if(document.querySelector("section .create-invitation") == null){
        $.ajax({
            url: '',
            method: 'POST',
            data: {
                csrfmiddlewaretoken: getCSRFToken(),
                action: 'createNewInvitation'
            },
            beforeSend: function(){
                // spinner fadeIn
                $("#loading").fadeIn(200);
            },
            success: function (data) {
                $("section .controls").append(data);
                console.log("Successfull");
            },
            error: function () {
                console.log("An error has occurred!");
            },
            complete: function(){
                // spinner fadeOut
                $("section .create-invitation").show('slow');

                $(".controls .add").fadeOut();
                $(".controls .cancel").fadeIn();

                $("#loading").fadeOut();
            }
        });
    }
    else {
        $("section .create-invitation").show('slow');
        $(".controls .add").fadeOut();
        $(".controls .cancel").fadeIn();
    }
}

function cancelNewInvitation(){
    $("section .create-invitation").hide('slow')
    $(".controls .cancel").fadeOut();
    $(".controls .add").fadeIn();
}



function getCSRFToken(){
    var array_cookies = document.cookie.split(";");
    for (var cookie in array_cookies){
        var array_cookie_split = array_cookies[cookie];
        if(array_cookie_split.trim().match(/csrftoken=\w+/g).length > 0){
            return array_cookie_split.split('=')[1];
        }
    }
}