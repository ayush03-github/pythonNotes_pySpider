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


// sort 

let randomNums = [100,23,234,345,567,2345,654,6543]
const sorted = randomNums.sort((a,b)=>{
    return a - b
})
console.log("sorted numbers ->", sorted)







// _______________________________________________________________________________

// MAP()



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