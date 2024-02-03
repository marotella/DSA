// Create a Phone Number

// Difficulty
// Medium
// Concepts
// General, Loops

// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// Example:

// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
// The returned format must be correct in order to complete this challenge.

// Don’t forget the space after the closing parentheses!

const createPhoneNumber = (num) => {
    //take the array
    // add it to a string in keeping order
    // insert phone number characters 
    phoneNumber = "("
    for(let i = 0; i < num.length; i++){
        if(i == 2){
            phoneNumber += num[i];
            phoneNumber += ") "
        }
        else if (i == 5){
            phoneNumber += num[i];
            phoneNumber += "-"
        }
        else{
            phoneNumber += num[i];
        }
     console.log(phoneNumber);
    }

}

createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);