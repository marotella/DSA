const best = (arr) =>{
    let profit = 0
    let minPrice = arr[0]
    
    for (let i =1; i<(arr.length); i++){
       let current_profit = arr[i] - minPrice
       if (current_profit > profit){
        profit = current_profit
       }
       if (arr[i] < minPrice){
        minPrice = arr[i]
       }
    }
    return profit
}

console.log(best([15, 10, 20, 22, 1, 9]))