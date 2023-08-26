//check authentication
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.dis');
    navLinks.forEach(link => {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        event.preventDefault();
        alert('You need to log in first.');
      });
    });
  });
// sign up request
document.getElementById('sign-up-form').addEventListener('submit', function(event) {
    const signUpButton = document.querySelector('#sign-up-btn[data-url]');
    const signUpUrl = signUpButton.getAttribute('data-url')
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);

    fetch(signUpUrl, {
        method: 'POST',
        body: formData,
        
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        
        if (data.success) {
            location.reload();
        } else {
            console.log(data.error_message)
            const errorMessageDiv = document.getElementById('error-message');
            errorMessageDiv.innerHTML = data.error_message;
        }
    });
});
// log in request
document.getElementById('log-in-form').addEventListener('submit', function(event) {
    const LogInButton = document.querySelector('#log-in-btn[data-url]');
    const LogInUrl = LogInButton.getAttribute('data-url')
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);

    fetch(LogInUrl, {
        method: 'POST',
        body: formData,
        
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        
        if (data.success) {
            location.reload();
        } else {
            
            const errorMessageDiv = document.getElementById('error-message');
            errorMessageDiv.innerHTML = data.error_message;
        }
    });
});
