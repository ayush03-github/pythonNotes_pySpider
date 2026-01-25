// // WAP to reverse a string.

// let institute = "pyspyder"

// str1 = ""
// for (let i = institute.length -1; i >= 0; i--){
//     str1 += institute[i]

// }
// console.log(str1)

// // WAP to check whether the given string is pallindrome or not 

// let str = "madam"

// strrev = ""
// for (let i = str.length -1; i >= 0; i--){
//     strrev += str[i]}
//     if (strrev === str){
//         console.log(`${str} is a pallindrome`)
//     }
//     else {
//         console.log(`${str} is not a pallindrome`)
//     }


// // BIULT-IN METHODS

// // 1. toUpperCase()

// let str3 = "dfghjkl"
// console.log(str3.toUpperCase())

// // 2. toLowerCase()

// let str4 = "I_Am_Ayush_Kodle"
// console.log(str4.toLowerCase())

// // 3. concat()
// let firstName = "John"
// let lastName = "Doe"
// let occupation = "Developer"    

// console.log(firstName.concat(" ", lastName," is a good", occupation))

// // 4. length
// let str5 = "Hello, World!"
// console.log("Length of the string is: ", str5.length)

// // 5. slice()
// let str6 = "JavaScript is awesome!"
// console.log(str6.slice(0, 10))  // Output: JavaScript
// console.log(str6.slice(11))     // Output: is awesome!


// // 6. replace()
// let str7 = "I love JavaScript"
// let newStr = str7.replace("JavaScript", "Python")
// console.log(newStr)  // Output: I love Python

// // 7, split()
// let str8 = "apple"
// let fruits = str8.split("")
// console.log(fruits)  // Output: [ 'a', 'p', 'p', 'l', 'e' ]
// let reversedStr = fruits.reverse()
// console.log(reversedStr)
// let joinedreversedStr = reversedStr.join("")
// console.log(joinedreversedStr)


// // or 
// console.log(str8.split("").reverse().join(""))

// // 8. trim()
// // removes extra whitespace (more than one) from both ends of a string

// let str9 = "   Hello, World!                                    "
// console.log("Before trim: '", str9, "'")
// console.log("After trim: '", str9.trim(), "'")


// // 9. padStart()
// let str10 = "5"
// console.log(str10.padStart(3,"0"))  // Output: 005
// console.log(str10.padEnd(4, "0"))    // Output: 5000

// const prompt = require("prompt-sync")({sigint: true});
// const mobile = prompt("Enter your mobile number: ")
// const lastThree = mobile.slice(-3)
// console.log(lastThree)
// const masked = lastThree.padStart(mobile.length, "*")
// console.log(masked)

// // OR

// const maskedNumber = mobile.slice(-3).padStart(mobile.length, "*")
// console.log(maskedNumber)


// 10. padEnd()

// let mail = prompt("Enter your mail id: ")

// let mailLength = mail.length

// let sliced = mail.slice(0,4)

// let maskedMail = sliced.padEnd(mailLength,"*")

// console.log(maskedMail)



// // 11. indexOf()

// let str11 = "ayushkodleuauduadugbuikua"
// console.log(str11.indexOf("u",4))


// //  12. charAt()

// let str12 = "characterAtWhichPosition"
// console.log(str12.charAt(5))

// // 13. charCodeAt()

// let str13 = "ABC"
// console.log(str13.charCodeAt(2))
// console.log(charCodeAt("a"))
// console.log(charCodeAt("A"))
// console.log(charCodeAt("z"))
// console.log(charCodeAt("Z"))

// 14. fromCharCode()

// console.log(String.fromCharCode(66))

const prompt = require("prompt-sync")({sigint: true})
let alpha = prompt("enter a charcter :")
console.log(alpha)
let alphaAscii = alpha.charCodeAt()
console.log("ASCII value of ", alpha, " is ", alphaAscii)
if (alphaAscii >= 97 && alphaAscii <= 122 ){
    for (let i = alphaAscii; i <= 123; i++){
    console.log(String.fromCharCode(i))}}
else
    for (let i = alphaAscii; i <= 90; i++){
    console.log(String.fromCharCode(i))}

