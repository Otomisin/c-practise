/**
 * In this example, we declare a function outerFunction() that declares a variable myVar with the value "hello" and then declares a new function innerFunction() that logs the value of myVar. We then return the inner function and assign it to a new variable myFunction. When we call myFunction(), it logs "hello", demonstrating the concept of closure.
 * 
 */
// Example of closure
function outerFunction() {
  let myVar = 'hello'; // declare a variable with the value "hello"

  function innerFunction() {
    console.log(myVar); // logs "hello"
  }

  return innerFunction; // return the inner function
}

let myFunction = outerFunction(); // assign the inner function to a new variable

myFunction(); // call the inner function, which logs "hello"
