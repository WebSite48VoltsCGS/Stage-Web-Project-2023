// Access DOM elements
const passwordInput = document.getElementById('password-input');
const confirmPassword = document.getElementById('confirm-password');
const errorMsg = document.getElementById('error-message');
const submitButton = document.getElementById('submit-button');

// Checks password confirmation
confirmPassword.addEventListener('blur', () => {
  if (passwordInput.value === confirmPassword.value) {
    submitButton.removeAttribute('disabled');
  } else {
    submitButton.setAttribute('disabled', 'true');
  }
});