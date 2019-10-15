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

$('#upload-photos').on('submit', function (event) {
    event.preventDefault();

    
    var files = $('#photos-input').get(0).files,
        formData = new FormData();

    if (files.length === 0) {
        alert('Select atleast 1 file to upload.');
        return false;
    }

    if (files.length > 1) {
        alert('You can only upload only 1 file.');
        return false;
    }

    for (var i=0; i < files.length; i++) {
        var file = files[i];
        formData.append('photos[]', file, file.name);
    }

    console.log(formData);
    uploadFiles(formData);
});



function uploadFiles(formData) {
    $.ajax({
        url: uploadUrl,
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        // xhr: function () {
        //     var xhr = new XMLHttpRequest();

        //     // Add progress event listener to the upload.
        //     xhr.upload.addEventListener('progress', function (event) {
        //         var progressBar = $('.progress-bar');

        //         if (event.lengthComputable) {
        //             var percent = (event.loaded / event.total) * 100;
        //             progressBar.width(percent + '%');

        //             if (percent === 100) {
        //                 progressBar.removeClass('active');
        //             }
        //         }
        //     });

        //     return xhr;
        // }
    }).done(handleSuccess).fail(function (xhr, status) {
        alert(status);
    });
}


function handleSuccess(data) {
    console.log(data);
    // if (data.length > 0) {
    //     // var html = '';
    //     // for (var i=0; i < data.length; i++) {
    //     //     var img = data[i];

    //     //     if (img.status) {
    //     //         html += '<div class="col-xs-6 col-md-12"><a href="#" class="thumbnail"><img src="' + img.publicPath + '" alt="' + img.filename  + '"></a></div>';
    //     //     } else {
    //     //         html += '<div class="col-xs-6 col-md-12"><a href="#" class="thumbnail">Invalid file type - ' + img.filename  + '</a></div>';
    //     //     }
    //     // }
    //     $("#convertBut").show();
    //     $('#upBut').hide();
    //     $('.progress').hide();
    //     // $('.progress-bar').width('0%');
    //     // $('#album').html(html);
    //     let img_path = data[0].publicPath;
    //     localStorage.setItem('img_path', JSON.stringify(img_path));
    // } else {
    //     alert('No images were uploaded.')
    // }
}





$('#photos-input').on('change', function () {
    $('.progress-bar').width('0%');
});







// $('#convertBut').on('click', function (event) {
  
//     let img_path = JSON.parse(localStorage.getItem('img_path'));
//     // console.log(img_path);
//     getXls(img_path);
// });






// function file_download()
// {
//     $.ajax({
//         url: '/download',
//         method:'get',
//         success: window.open('/download'),
//     }).done(function(){
//         alert("Your file has been downloaded!");
//     }).fail(function(){
//         alert("Could not download the file!");
//     })
// }


// function getXls(img_path) {
//     alert("Your file is being processed!");
//     $.ajax({
//         url: '/generate_xls',
//         method: 'post',
//         data: {
//             "img":img_path
//         },
//         headers: {
//             "Content-Type": 'application/x-www-form-urlencoded',
//             "charset": "utf-8"
//         }
     
//     }).done(function(){ 
//         alert("Excel File Generated!");
//         file_download();
//     }).fail(function () {
//         alert("Error in generating Excel File!!!");
//     });
// }