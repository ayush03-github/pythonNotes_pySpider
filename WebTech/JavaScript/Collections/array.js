// arrays are the container to store multiple data 
// Eg: we can store multi contact number in an array 
// let arr = [val1, val2, val3,.....]

// Arrays are heterogeneous

// These are ordered 

// These are mutable in nature

// supports duplicate

// supports only positive indexing

// supports slicing


// ________________________________________________________________________________________________________________________________________


// Built-In methods

let skills = ["HTML" , "CSS", "JAVASCRIPT", "PYTHON", "DJANGO", "REACTJS", "SQL", "NEXTJS"]

console.log("LIST OF SKILLS: ", skills)
console.log(typeof skills)
console.log("first skill is : ", skills[0])

// 1. toString: converts whole array into a string

let strSkills = skills.toString()
console.log("1. toString ", strSkills)
console.log(typeof strSkills)

//2. join() : Joins all the elements of array using give seperator


// 3. pop() : Remove last element for the array  and returns it

console.log(skills.pop())

console.log(skills.pop())


// 4. push() 

console.log(skills.push("Angular"))
console.log(skills)

// 5. shift() : removes element form beginning of array and return the length 

console.log(skills.shift())
console.log(skills)

//  6. unShift() : add element to the beginning of array and returns the count

console.log(skills.unshift("Git"))
console.log(skills)

//  7. length

console.log(skills.length)

// 8. slice

console.log(skills.slice(2,5))

// 9. splice

console.log("original array :", skills)
skills.splice(0, skills.length, "removed all skills and added this")
console.log("splicing :",skills)


skills.push("Full Stack Development")
console.log(skills)
// 10. reverse

skills.reverse()
console.log(skills)


// 11. sort 

let randomNums = [100,23,234,345,567,2345,654,6543]
const sorted = randomNums.sort((a,b)=>{
    return a - b
})
console.log("sorted numbers ->", sorted)







// _______________________________________________________________________________

// 12. MAP()



// /Write javascript code to display products in E-commerce website

const products = [
  {
    id: 1,
    category: "electronics",
    brand: "Skullcandy",
    description: "A true wireless headset for your best sound experience",
    stockAvailability: 10,
    price: 5999,
    image: "https://m.media-amazon.com/images/I/71XV1uzAw8L._AC_UY327_FMwebp_QL65_.jpg",
  },
  {
    id: 2,
    category: "smartphone",
    brand: "Apple",
    description: "iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Teal",
    stockAvailability: 10,
    price: 119999,
    image: "https://m.media-amazon.com/images/I/71XV1uzAw8L._AC_UY327_FMwebp_QL65_.jpg",
  },
  {
    id: 3,
    category: "Cameras",
    brand: "Sony",
    description: "A 12D mirrorles camera for capturing the life in the moment",
    stockAvailability: 2,
    price: 299999,
    image: "https://m.media-amazon.com/images/G/31/img25/Camera/clp/1._CB774306738_.jpg",
  }
];


products.map((products)=>{
    
    console.log("id :", products.id)
    console.log("category :", products.category)
    console.log("brand", products.brand)
    console.log("description", products.description)
    console.log("stock Availiabilty :", products.stockAvailability)
    console.log("price", products.price)

})
// ____________________________________________________________________________________________________________________


// 13. filter() 
// : is udes to filter out the value with repect to the condition provided


let num = [1,2,3,4,5,6,7,8,9,10]
let divThree = num.filter((item) => {
    return item % 3 == 0
})
console.log(divThree)


// ____________________________________________________________________________________________________________________
// 14. reduce()
// : is used to reduce the array to a single value based on the logic provided

let nums = [1,2,3,4,5,6,7,8,9,10]
 sum = nums.reduce((acc,curVal) => {
  return acc ** curVal
 })
console.log(sum)


// ____________________________________________________________________________________________________________________

// 15. forEach()
// : is used to iterate over each element of the array

let numbers = [10,20,30,40,50]

numbers.forEach((item)=>{
    console.log(item)
})

// note :'map()' returns a new array whereas 'forEach()' does not returns individual value

// ____________________________________________________________________________________________________________________

// 16. some()
// : checks if atleast one element in the array satisfies the given condition

let number = [2,4,6,8,10,11]

let isOdd = number.some((item)=>{
    return item % 2 != 0
})  

console.log(isOdd)  // true

// ____________________________________________________________________________________________________________________

// 17. every()
// : checks if all the elements in the array satisfies the given condition    

let number1 = [2,4,6,8,10,12]

let allEven = number1.every((item)=>{
    return item % 2 == 0
})    
console.log(allEven)  // true

// ____________________________________________________________________________________________________________________


// 18. flat()
// : is used to flatten the nested array into single array
let nestedArray = [1,2,[3,4],[5,6],[7,8,9]]
let flatArray = nestedArray.flat()
console.log(flatArray)  // [1,2,3,4,5,6,7,8,9]

let nestedArray2 = [1,2,[3,4],[5,6,[3,4],[5,6]],[7,8,9]]
let flatArray2 = nestedArray2.flat(2)
console.log(flatArray2)  // [1,2,3,4,5,6,3,4,5,6,7,8,9]

let nestedArray3 = [1,2,[3,4],[5,6,[3,4,[9,10,[5,6,[3,4,[9,10]]]],[5,6]]],[7,8,9]]
let flatArray3 = nestedArray3.flat(Infinity)
console.log(flatArray3)  // [1,2,3,4,5,6,3,4,9,10,5,6,3,4,9,10,5,6,7,8,9]

// ____________________________________________________________________________________________________________________

// destructuring of array
// defination: Assigning a value to a distinct variable by unpacking it from array collection
let colors = ["Red", "Green", "Blue", "Yellow"]

let [color1, color2, color3, color4] = colors 
console.log(color1)  // Red
console.log(color2)  // Green
console.log(color3)  // Blue
console.log(color4)  // Yellow