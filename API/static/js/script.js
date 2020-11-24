$(document).ready(function () {
    $("#file").on("change", function (){
        var previewUploadImage = document.getElementById("upload_image")
        var previewOutputImage = document.getElementById("output_image")
        var file    = document.getElementById("file").files[0];
        var reader  = new FileReader();

        reader.onloadend = function () {
            previewUploadImage.src = reader.result;
            previewOutputImage.src = "static/frame.jpg"
        }

        if (file) {
            reader.readAsDataURL(file);
        } else {
            previewUploadImage.src = "";
            previewOutputImage.src = "";
        }
    } );
});