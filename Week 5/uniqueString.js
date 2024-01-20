//Write a function to remove all duplciate letters from a provided string. The string will only contail lowercase letters between a - z. The string will not contain spaces.

const makeUnique = (string) =>{
    let unique = "";
    for(const letter of string){
        if(!unique.includes(letter)){
            unique += letter
        }
    }
    return unique
}

console.log(makeUnique("helloworld"))