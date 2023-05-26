// Example of variable declaration and scope
let myVar = 'hello'; // declare a variable of type string with the value "hello"

function myFunction() {
  let myVar = 'world'; // declare a new variable of the same name with a different value
  console.log(myVar); // logs "world"
}

myFunction(); // calls the function and logs "world"
console.log(myVar); // logs "hello"
