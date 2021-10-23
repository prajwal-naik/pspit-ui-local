$(document).ready(function(){
    $(document).on("click", ".submitButton", function(event) {
        event.preventDefault();
        var port = $("#port").val();
        var message = $("#message").val();
        var formData = $("#demoForm")[0];
        var data = new FormData(formData);


        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/startDemo",
            data: data,
            processData: false,
            contentType: false,
            // cache: false,
            // timeout: 800000,
            success: function (data) {
                // console.log(data);
                $("#res").val(data);
                // console.log("SUCCESS : ", data);
                // $("#btnSubmit").prop("disabled", false);
 
            }
            // ,
            // error: function (e) {
 
            //     $("#output").text(e.responseText);
            //     console.log("ERROR : ", e);
            //     $("#btnSubmit").prop("disabled", false);
 
            // }
        });
    });
});