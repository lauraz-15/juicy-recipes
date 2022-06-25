
// Time out function for user messages/feedback

  setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


function texting() {
    console.log("Main js file is connected on this page!")
}

texting();