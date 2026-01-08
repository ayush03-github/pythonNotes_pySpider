// conditional statements in JavaScript are used to perform different actions based on different conditions. The most common conditional statements are `if`, `else if`, `else`, and `switch`.

// let age = 20

// if (age < 18) {
//     console.log("You are a minor.")
// }
// else if (age >= 18 && age < 65) {
//     console.log("You are an adult.")
// }
// else {
//     console.log("You are a senior citizen.")
// }

// // switch statement
// let day = 3
// let dayName = ""    
// switch (day) {
//     case 1:
//         dayName = "Monday"
//         break
//     case 2:
//         dayName = "Tuesday"
//         break
//     case 3:
//         dayName = "Wednesday"
//         break
//     case 4:
//         dayName = "Thursday"
//         break
//     case 5:
//         dayName = "Friday"
//         break
//     case 6:
//         dayName = "Saturday"
//         break
//     case 7:
//         dayName = "Sunday"
//         break
//     default:
//         dayName = "Invalid Day Number"
// }
// console.log("Today is:", dayName)

// -------------------------------------------------------------

// const prompt = require("prompt-sync")()
// const username = prompt("Enter your username:")
// const password = prompt("Enter your password:")
// if(username === "admin" && password === "12345") {
//     console.log("Login successful!")
// } else {
//     console.log("Invalid username or password.")
// }


// --------------------------------------------------------------

// const speed = prompt("enter your speed: ")

// if (speed > 0 && speed <= 60) {
//     console.log("Driving too slow.")
// }else if (speed > 60 && speed <= 120) {
//     console.log("Noarmal speed.")
// }else if (speed > 120 && speed <= 200) {
//     console.log("Driving too fast.")
// }else {
//     console.log("Welcome to the heaven.")
// }



// nested if else


// const email = prompt("Enter your email: ")
// if (email === "ayushkodle1@gmail.com") {
//     const pwd = prompt("Enter your password: ")
//     if (pwd === "Ayush@123") {
//         console.log("Login successful!")
//     } else {
//         console.log("Invalid password.")
//     }
// }else {
//     console.log("Invalid email.")
// }


// switch case example

// const day = 1
const day = new Date().getDay()
let result 

switch (day) {
    case 0:
        result = "Sunday"
        break
    case 1:
        result = "Monday"
        break
    case 2:
        result = "Tuesday"
        break
    case 3:
        result = "Wednesday"
        break
    case 4:
        result = "Thursday"
        break
    case 5:
        result = "Friday"
        break
    case 6:
        result = "Saturday"
        break
    default:
        result = "Invalid day number"
}
console.log(`today is: ${result}`)