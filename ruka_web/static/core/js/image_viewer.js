    $(document).ready(function() {
    $('.copyte').each(function(index, element) {
    $(element).click(function() {
        var clickedTdText = $(this).text() //get the clicked text
        var temp = $("<input>"); //create temp  input
        $("body").append(temp); //append temp input
        temp.val(clickedTdText).select(); //select text
        document.execCommand("copy");
        temp.remove(); //remove temp inout
        
    })
    })
});

// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var imgs = document.getElementsByClassName('myImg');
var modalImg = document.getElementById("img01");
var modalImg2 = document.getElementById("img02");
var captionText = document.getElementById("caption");
Array.prototype.forEach.call(imgs, function(img) {
img.onclick = function() {
modal.style.display = "block";
modalImg.src = this.src.replace("/125x125/", "/");
modalImg2.src = this.src;
captionText.innerHTML = this.alt;
}
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("modal")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
modal.style.display = "none";
}

function cerrar(){
closePopup()
};
const copyURL = () => {
const copyDiv = document.querySelector('.copyAlert:not(.animate)')
if(copyDiv) {
    copyDiv.classList.add('animate');
    copyDiv.addEventListener('animationend', () => copyDiv.classList.remove('animate') );
}
};
var btn = $('#button');

$(window).scroll(function() {
if ($(window).scrollTop() > 300) {
    btn.addClass('show');
} else {
    btn.removeClass('show');
}
});

btn.on('click', function(e) {
e.preventDefault();
$('html, body').animate({scrollTop:0}, '300');
});