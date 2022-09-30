let sender = document.getElementById('contact_name').value
let email = document.getElementById('contact_email').value
let message = document.getElementById('contact_message').value
let sendMail = document.getElementById('send-mail') 

sendMail.addEventListener('click', function(event){
    event.preventDefault()
    emailjs.send("contact_service", "contact_form", {
        "contact_name": sender,
        "contact_email": email,
        "contact_message": message,
    })
        .then(
            function (response) {
                console.log("SUCCESS", response.status);
            },
            function (error) {
                console.log("FAILED", error);  
            }
        );
})