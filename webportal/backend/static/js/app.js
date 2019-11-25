console.log("Connected");
$("#convertBut").hide();


//Validating Cross Origin Post Requests in Django

var csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
})

$('#upload').on('submit', function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    
    $.ajax({
        url: uploadUrl,
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        xhr: function () {
            var xhr = new XMLHttpRequest();

            // Add progress event listener to the upload.
            xhr.upload.addEventListener('progress', function (event) {
                var progressBar = $('.progress-bar');

                if (event.lengthComputable) {
                    var percent = (event.loaded / event.total) * 100;
                    progressBar.width(percent + '%');

                    if (percent === 100) {
                        progressBar.removeClass('active');
                    }
                }
            });

            return xhr;
        },
        success: function() {
            $("#convertBut").show();
            $('#upBut').hide();
            $('.progress').hide();
        },
        error: function(){
            alert(status);
            $('.progress').hide();
        }
    });
});

$('#imageIp').on('change', function () {
    $('.progress-bar').width('0%');
});



$('#convertBut').on('click', function (event) {
    $('#overlay').show();
    alert("Your file is being processed!");
    $.ajax({
        url: generateXlsUrl,
        method: 'GET',
        error: function () {
            alert("Error in generating Excel File!!!");
            $('#overlay').hide();
        },
        success: function(data){ 
            $('#overlay').hide();
            alert("Excel File Generated!");
            file_download();
            // console.log(data);
        }

    })
});




function file_download()
{
    $.ajax({
        url: downloadUrl,
        method:'get',
        success: window.open(downloadUrl),
    }).done(function(){
        alert("Your file has been downloaded!");
    }).fail(function(){
        alert("Could not download the file!");
    })
}


