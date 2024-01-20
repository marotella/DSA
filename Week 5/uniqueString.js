//Write a function to remove all duplciate letters from a provided string. The string will only contail lowercase letters between a - z. The string will not contain spaces.

const makeUnique = (str) =>{
    let unique = "";
    for(let i =0; i<str.length; i++){
        if(!unique.includes(str[i])){
            unique += (str[i])
        }
    }
    return unique
}

console.log(makeUnique("helloworld"))