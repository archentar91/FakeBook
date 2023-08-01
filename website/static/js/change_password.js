
const passwordInput = document.getElementById("id_new_password1");
const confirmPasswordInput = document.getElementById("id_new_password2");
const passwordMismatchMsg = document.getElementById("password-mismatch-msg");
const passwordStrengthMsg = document.getElementById("password-strength-msg");
const changePassButton = document.getElementById("changePass-btn");

// Function to check if the password meets the minimum length requirement (e.g., 8 characters)
function isPasswordValid(password) {
    return password.length >= 8;
}

// Function to check if the password has medium strength (contains numbers and letters)
function hasMediumStrength(password) {
    const hasLetters = /[a-zA-Z]/.test(password);
    const hasNumbers = /\d/.test(password);
    return hasLetters && hasNumbers;
}

// Function to check if the password has strong strength (contains letters, numbers, and special characters)
function hasStrongStrength(password) {
    const hasLetters = /[a-zA-Z]/.test(password);
    const hasNumbers = /\d/.test(password);
    const hasSpecialChars = /[!@#$%^&*()_+[\]{};':"\\|,.<>?]/.test(password);
    return hasLetters && hasNumbers && hasSpecialChars;
}

function updateChangePasswordButtonState() {
    if (passwordInput.value === confirmPasswordInput.value && isPasswordValid(passwordInput.value)) {
        changePassButton.disabled = false;
    } else {
        changePassButton.disabled = true;
    }
}

function updatePasswordValidity() {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;
    const isValidPassword = isPasswordValid(password);

    // Password Strength Feedback
    if (password === "") {
        passwordStrengthMsg.textContent = ""; // Hide strength feedback when password field is empty
    } else {
        if (isValidPassword) {
            if (hasStrongStrength(password)) {
                passwordStrengthMsg.textContent = "Strong password";
                passwordStrengthMsg.style.color = "#4CAF50"; // Green
            } else if (hasMediumStrength(password)) {
                passwordStrengthMsg.textContent = "Medium password";
                passwordStrengthMsg.style.color = "#FFA500"; // Orange
            } else {
                passwordStrengthMsg.textContent = "Weak password";
                passwordStrengthMsg.style.color = "#FF5722"; // Red
            }
        } else {
            passwordStrengthMsg.textContent = "Password should be at least 8 characters";
            passwordStrengthMsg.style.color = "#FF5722"; // Red
        }
    }

    // Password Mismatch Feedback
    if (confirmPassword === "") {
        passwordMismatchMsg.textContent = ""; // Hide mismatch feedback when confirmation field is empty
    } else {
        if (password === confirmPassword) {
            passwordInput.style.backgroundColor = isValidPassword ? "#E8F5E9" : "#FFEBEE"; // Light Green / Light Red
            confirmPasswordInput.style.backgroundColor = isValidPassword ? "#E8F5E9" : "#FFEBEE"; // Light Green / Light Red
            passwordMismatchMsg.textContent = "";
        } else {
            passwordInput.style.backgroundColor = "#FFEBEE"; // Light Red
            confirmPasswordInput.style.backgroundColor = "#FFEBEE"; // Light Red
            passwordMismatchMsg.textContent = "Passwords do not match!";
        }
    }

    updateChangePasswordButtonState();
}

function updateConfirmPassword() {
    const password = passwordInput.value;
    if (password === "") {
        confirmPasswordInput.value = ""; // Set password2 to empty if password1 is empty
        confirmPasswordInput.style.backgroundColor = ""; // Reset background color
        passwordInput.style.backgroundColor = ""; // Reset background color
        passwordStrengthMsg.textContent = ""; // Hide strength feedback when password field is empty
        passwordMismatchMsg.textContent = ""; // Hide mismatch feedback when confirmation field is empty
    }
}

// Remove password strength feedback and password mismatch error on initial page load
passwordStrengthMsg.textContent = "";
passwordMismatchMsg.textContent = "";

confirmPasswordInput.addEventListener("input", updatePasswordValidity);
passwordInput.addEventListener("input", updatePasswordValidity);

// Add the event listener for updating password2 when password1 is empty
passwordInput.addEventListener("input", updateConfirmPassword);

// Call the function on page load to initialize the button state and password2
updatePasswordValidity();
updateConfirmPassword();

