//Given a number, n, return an array containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

// You can trust that this function will never be called with n < 0 or n > 10.

function luckyNumber(n) {
    const numList = []
    for (let i = 1; i < n;) {
        let randomNum = Math.floor(Math.random() * 10) + 1
        if (numList.includes(randomNum) === false) {
            numList.push(randomNum)
            i = i + 1
        }
    }
    return numList
}

console.log(luckyNumber(5))