// A function which accepts another function as its parameter is called higher order function or callback function
// when a function is passed a parameter to an another function

function outer(){
    console.log("outer function")

}
function inner(){
    console.log("inner function")

}

outer(inner())


// Eg:

//  sort
//  Map
//  forEach
//  promise