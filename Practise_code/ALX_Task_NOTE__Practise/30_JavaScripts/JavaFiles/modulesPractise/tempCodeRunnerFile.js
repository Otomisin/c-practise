// Importing a module that uses Named Exports
import { greet, PI, Person } from './myModule.js';

greet('Alice');   // Output: Hello, Alice!
console.log(PI);  // Output: 3.14159
const p = new Person('Bob', 30);
console.log(p);   // Output: Person { name: 'Bob', age: 30 }

// // Importing a module that uses Default Exports
// import myMessage from './myModule.js';
// import Rectangle from './myModule.js';

// console.log(myMessage);      // Output: Hello, World!
// console.log(new Rectangle(5, 10).area);  // Output: 50
