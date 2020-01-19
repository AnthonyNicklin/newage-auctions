// When the user scrolls down 20px from the top of the document, show the button.
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("topBtn").style.display = "block";
    } else {
        document.getElementById("topBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document.
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Modal
function modal() {
    const modal = document.getElementById('myModal');
    const closeCross = document.getElementsByClassName("close-cross")[0];
    const closeBtn  = document.getElementById('close');

    modal.style.display = "block";

    //Hide the modal when the x is clicked
    closeCross.onclick = function() {
    modal.style.display = "none";
    };

    //Hide the modal when the close button is clicked
    closeBtn.onclick = function() {
    modal.style.display = "none";
    };

    //Close when the user clicks anywhere outside the modal
    window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
        }
    };
};
