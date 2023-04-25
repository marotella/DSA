// Given an integer n, return a counter function. This counter function initially returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let counter = n
    return function() {
        let current = counter
        counter++
        return current
        
    };
};

//Given a positive integer millis, write an asyncronous function that sleeps for millis milliseconds. It can resolve any value.

/**
 * @param {number} millis
 */
async function sleep(millis) {
    return new Promise ((resolve) =>{
    let t = Date.now()
    setTimeout(() => {
        resolve(console.log(Date.now() - t))}, millis)
    })
}
