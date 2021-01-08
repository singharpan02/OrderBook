function onClickFeedback() {
    alert('Your response has been submitted');
}

function homeActive() {
    document.getElementById("home").classList.add("active");
}

function sharesActive() {
    document.getElementById("home").classList.remove("active");
    document.getElementById("shares").classList.add("active");
}

function aboutActive() {
    document.getElementById("home").classList.remove("active");
    document.getElementById("about").classList.add("active");
}

function contactActive() {
    document.getElementById("home").classList.remove("active");
    document.getElementById("contact").classList.add("active");
}
