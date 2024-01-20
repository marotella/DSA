const printDigits = (num) => {
    if (num > -10 && num < 10){
        console.log(num)
    } else {
        while(num !== 0){
            const digit = num % 10
            console.log(digit)
            num = Math.floor(num/10)
        }
    }
}


printDigits(1)
// 1

printDigits(314)
// 4
// 1
// 3

printDigits(12)