// Immediately Invoked Functons Expressions

// the functions which calls themselves right after their declaration

(function() {
    let a = 100
    let b = 133
    let c = a + b
    console.log(c)
    console.log("IIFE 1: This function runs immediately after it's defined.");
})(console.log("IIFE 2: This is another example of an IIFE."));


const prompt  = require("prompt-sync")({sigint: true})

const n = prompt("Enter a number : ")
let arr = []

for(i = 1; i<= n;i++){
    const ele = parseInt(prompt(`enter ${i} number :`)) 
    arr.push(ele)   
}
console.log(arr)
const squares = arr.map((item) => {
    return item ** 2
})
console.log(squares)

const cubes = arr.map((item) => {
    return `${item} X ${item} X ${item} is ${item ** 3}`
})
console.log(cubes)



// _______________________________________________________________________________

// IIFE to calculate factorial of a number

const num = prompt("Enter a number to find factorial : ")
let fact = 1

;(function factorial(n){
    for(let i = 1; i <= n; i++){
        fact = fact * i
    }
    console.log(`Factorial of ${n} is ${fact}`)
})(num) 
// _______________________________________________________________________________

