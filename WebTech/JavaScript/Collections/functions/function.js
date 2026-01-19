// functiond in js




// function with return keyword

const add = (...nums) => {
    let sum = 0;    
    for(let n of nums){ 
        sum += n
    }
    return sum;
}   

let result = add(1,2,3,4,5,6,7,8,9,10)
console.log("Sum is : ", result)