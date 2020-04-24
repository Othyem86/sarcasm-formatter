// 
//  MAIN PROGRAM
// 

// Alternates capitalisation in string of first argument. Starts with capitalization based on second bool argument
const alterNate = (input, bool) => {

    let str = '';
    let lowerCase = bool;

    // Interates through input string
    for (let i = 0; i < input.length; i++) {

        // Check only non-space, non-numeric characters
        if (/[\S\D]/ig.test(input[i])) {

            // Capitalizes alternatively
            if (lowerCase === false) {
                str += input[i].toUpperCase();
                lowerCase = true;
            } else {
                str += input[i].toLowerCase();
                lowerCase = false;
            }

        // Leave space and numeric values as they were
        } else {
            str += input[i];
        }
    }

    // Return formatted string
    return str;
}


// Formats the user inputs each button click
function sarcasmFormatter() {
    // Gets user input from textarea
    let userTextInput = document.getElementById("user-input").value;

    // Checks if Start with lower case checkbox is checked
    let checkLowerCase = document.getElementById("checkLowerCase").checked;

    // Formats the text from the user input and returns it to the result textarea
    document.getElementById("result").value = alterNate(userTextInput, checkLowerCase);
}