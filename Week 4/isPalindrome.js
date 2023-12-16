// Return true if this word is a palindrome. false if it is not. A palindrome is a word that is spelled the same backwards and forwards.

function isPalindrome(str) {
    str = str.toLowerCase()
    let strArray = str.split("")
    strArray.reverse()
    let reverseStr = strArray.join("")
    if( reverseStr === str){
        return true
    } else {
        return false
    }


}