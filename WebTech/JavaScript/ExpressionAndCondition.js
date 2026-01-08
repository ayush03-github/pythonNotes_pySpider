// * Expression and Condition
// Expressions are combinations of values, variables, operators, and functions that are evaluated to produce a value.

// Piece of code that produces a value is called an expression.

// Arithematic Expressions
let a = 10
let b = 4
console.log(`The sum of ${a} and ${b} is: ${a + b}`)
console.log(`The difference of ${a} and ${b} is: ${a - b}`)
console.log(`The product of ${a} and ${b} is: ${a * b}`)
console.log(`The division of ${a} and ${b} is: ${a / b}`)


// increment and decrement
let c = 5   
 //pre-increment
 ++c
 console.log("Value of c after pre-increment is:",c)    
//pre-decrement
--c
console.log("Value of c after pre-decrement is:",c)
// post-increment
console.log("Value of c after post-increment is:",c++) //5
console.log("Value of c now is:",c) //6
//post-decrement
console.log("Value of c after post-decrement is:",c--) //6
console.log("Value of c now is:",c) //5

console.log("***************************************")
a = 23

console.log(++a)
console.log(--a)
console.log(a++)
console.log(--a)
console.log(a--)
console.log(a)

console.log("***************************************")

// Assignment operators                   

let x = 10
let y = 5

console.log("x = ", x)
console.log("y = ", y)

x += 5
console.log("x += 5:", x)

y -= 2
console.log("y -= 2:", y)

x *= 3
console.log("x *= 3:", x)

y /= 2
console.log("y /= 2:", y)

x %= 4
console.log("x %= 4:", x)
y **= 3
console.log("y **= 3:", y)
console.log("***************************************")



// Comparison Operators
let p = 7
let q = 10
let m = 100
let n = "100"
let o = 100  
console.log("p = ", p)
console.log("q = ", q)  
console.log("p == q:", p == q)                               // false
console.log("p != q:", p != q)                               // true
console.log("m === n:", m === n)                             // false   
console.log("m === o:", m === o)                             // true
console.log("m !== n:", m !== n)                             // true
console.log("p !== q:", p !== q)                             // true
console.log("p > q:", p > q)                                 // false
console.log("p < q:", p < q)                                 // true
console.log("p >= q:", p >= q)                               // false
console.log("p <= q:", p <= q)                               // true 
console.log("***************************************")

//ternary operator
let age = 20
let canDrive = (age >= 18) ? "Yes, you can drive." : "No, you cannot drive."
console.log("Age:", age)
console.log("Can I drive?:", canDrive)


// Logical Operators

// AND (&&) Operator
// returns true when both the values are true
//  ____________________________________                 
// |v1      |  v2        |   result     |            
// |--------|------------|------------- |                
// |True    |  True      |   True       |          
// |True    |  False     |   False      |           
// |False   |  True      |   False      |           
// |False   |  False     |   False      |     

let ayush = 22
let shubham = 25

let canAyushVote = (ayush >= 18) && (ayush <= 60) ? "Yes, Ayush can vote." : "No, Ayush cannot vote."
let canShubhamVote = (shubham >= 18) && (shubham <= 60) ? "Yes, Shubham can vote." : "No, Shubham cannot vote."


// OR (||) Operator
// returns true when at least one of the values is true
//  ____________________________________                     
// | v1      |  v2        |   result    |                  
// |---------|------------|-------------|                     
// | True    |  True      |   True      |               
// | True    |  False     |   True      |               
// | False   |  True      |   True      |               
// | False   |  False     |   False     |   


// NOT (!) Operator
// returns the opposite boolean value
//  ______________________
// | v1      |   result   |
// |---------|------------|
// | True    |   False    |
// | False   |   True     |



