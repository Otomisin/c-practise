/**
 * In this example, we declare a constructor function Person() that creates objects with properties name and age. We then add a new method greet() to the prototype of the constructor function, which logs a greeting message using the object's name and age properties. We create two new Person objects using the new keyword and then call the greet() method on each object, demonstrating the concept of prototypes in JavaScript.
 */

// Example of prototype
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function() {
  console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
};

let person1 = new Person('Alice', 25); // create a new Person object
let person2 = new Person('Bob', 30); // create another Person object

person1.greet(); // logs "Hello, my name is Alice and I am 25 years old."
person2.greet(); // logs "Hello, my name is Bob and I am 30 years old."
