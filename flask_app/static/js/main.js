document.getElementById("survey_form").addEventListener("submit", validateForm);

function validateForm(event) {
    let isValid = true;

    let dropdowns = document.querySelectorAll(".dropdown");
    
    let athlete = document.getElementById("athlete");

    dropdowns.forEach((dropdown) => {
        let errorElement = dropdown.nextElementSibling; // Get the next <p> for error
        if (dropdown.value === "") {
            errorElement.textContent = "Please select an option.";
            isValid = false;
        } else {
            errorElement.textContent = "";
        }
    });

    let textInputs = document.querySelectorAll(".text_input");
    textInputs.forEach((input) => {
        let errorElement = input.nextElementSibling; // Get the next <p> for error
        if (input.value.trim() === "") {
            errorElement.textContent = "This field cannot be empty.";
            isValid = false;
        } else {
            errorElement.textContent = "";
        }
    });

    let how_long = document.getElementById("how_long");
    let number_error = document.getElementById("number_error");
    
    if (how_long.value.trim() === "") {
        how_long.textContent = "Please enter a number.";
        isValid = false;
    } else if (isNaN(how_long.value) || Number(how_long.value) < 0 || Number(how_long.value) > 100) {
        number_error.textContent = "Enter a number between 0 and 100";
        isValid = false;
    } else {
        number_error.textContent = "";
    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission
    }
}