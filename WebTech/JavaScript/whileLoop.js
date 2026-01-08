// works based on condition
// gets executed until the condition evaluates as False

const prompt = require("prompt-sync")({sigint: true});

let n = parseInt(prompt("enter a number: "))

 let temp = -n
while(n >= temp){
    console.log(n)
    n--

}