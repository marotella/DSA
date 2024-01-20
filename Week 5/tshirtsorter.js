//
// Write a function that will take in a string containing only s, m, and l characters. Ex: slsmmsllsmsmlmsls

// This string essentially represents a bunch of t-shirts in an unsorted pile. Your function should return this pile of t-shirts sorted by small, then medium, then large. The above example would be returned sssssssmmmmmlllll.

// The given string will never include characters outside of the lowercase s, m, and l. The string will also never contain any spaces.

const tShirtSorter = (string) =>{
    let s = "";
    let m = "";
    let l = "";
    for (const letter of string){
        if(letter === "s"){
            s += letter
        } else if(letter === "m"){
            m += letter
        } else if( letter === "l"){
            l += letter
        }
    }
    return s + m + l
}

console.log(tShirtSorter("lmsslmslls"))