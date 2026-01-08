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
