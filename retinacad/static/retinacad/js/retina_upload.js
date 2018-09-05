document.getElementById("lefteye").onchange = function () {
    var reader = new FileReader();

    reader.onload = function (e) {
        // get loaded data and render thumbnail.
        var image = document.getElementById("leyeimg")
        image.src = e.target.result;
        image.width = 250; // a fake resize
    };

    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
};

document.getElementById("righteye").onchange = function () {
    var reader = new FileReader();

    reader.onload = function (e) {
        // get loaded data and render thumbnail.
        var image = document.getElementById("reyeimg")
        image.src = e.target.result;
        image.width = 250; // a fake resize
    };

    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
};