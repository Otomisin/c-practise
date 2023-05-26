#!/usr/bin/node
// Importing a module that uses Named Exports
import { greet, PI, Person } from './myNamedModule.js';

greet('Alice');   // Output: Hello, Alice!
console.log(PI);  // Output: 3.14159
const p = new Person('Bob', 30);
console.log(p);   // Output: Person { name: 'Bob', age: 30 }
alert(PI)


// // Importing a module that uses Default Exports
// import myMessage from './myDefaultModule.js';
// import Rectangle from './myDefaultModule.js';

// console.log(myMessage);      // Output: Hello, World!
// console.log(new Rectangle(5, 10).area);  // Output: 50
