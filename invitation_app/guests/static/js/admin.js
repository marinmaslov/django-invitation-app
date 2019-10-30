/* CREATE NEW INVITATION */
function createNewInvitation() {
    if(document.querySelector(".create-invitation") == null){
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
                $(".invitations-container").prepend(data);
                console.log("Successfull");
            },
            error: function () {
                console.log("An error has occurred!");
            },
            complete: function(){
                // spinner fadeOut
                $(".create-invitation").show('slow');
                $("#loading").fadeOut();
            }
        });
    }
    else {
        $(".create-invitation").remove();
        createNewInvitation();
    }
}


/* CANCLE NEW INVITATION */
function cancelNewInvitation(){
    $(".create-invitation").hide('slow');
}

/* SUBMIT INVITATION */
function submitInvitation() {
    $.ajax({
        url: '',
        method: 'POST',
        data: {
            csrfmiddlewaretoken: getCSRFToken(),
            action: 'submitInvitation',
        },
        beforeSend: function(){
            // spinner fadeIn
            $("#loading").fadeIn(200);
        },
        success: function (data) {
            console.log(data + "Successfull");
        },
        error: function () {
            console.log("An error has occurred!");
        },
        complete: function(){
            // spinner fadeOut
            $("#loading").fadeOut();
        }
    });
}





/* CSRF TOKEN */
function getCSRFToken(){
    var array_cookies = document.cookie.split(";");
    for (var cookie in array_cookies){
        var array_cookie_split = array_cookies[cookie];
        if(array_cookie_split.trim().match(/csrftoken=\w+/g).length > 0){
            return array_cookie_split.split('=')[1];
        }
    }
}


/* COPY TO CLIPBOARD */
function copyToClipBoard(e){
    let string = e;
    let element = string.childNodes[3].childNodes[0];
    element.select();
    document.execCommand('copy');

    $('#message').fadeIn(500, function(){
        $('#message').fadeOut(500);
    });
}