const fruits = ["Banana", "Orange", "Apple", "Mango"];
const fruit2 = ["Peer"];
console.log(fruits);
console.log(fruits[2]); // using []
console.log(fruits.at(3)); // using .at()

const allfruit = fruits.concat(fruit2); // Concate two arrays
console.log(allfruit); 

const allfruitn = allfruit.concat("Carrot") //Merging an array with values 
console.log(allfruitn);




// FILTER///////////////////////////
// // Example 1: Filtering an array of objects based on a property value

// /**
//  * In this example, we have an array of objects representing different products. We want to filter the array to only include products that cost more than $1. We use the filter() method with a callback function that checks the price property of each object
//  * 
//  */
// const products = [
//   { name: 'Apple', price: 1.5 },
//   { name: 'Banana', price: 0.5 },
//   { name: 'Cherry', price: 2.0 },
//   { name: 'Durian', price: 5.0 },
// ];

// console.log(typeof(products));

// // Filter products that cost more than $1
// const expensiveProducts = products.filter(product => product.price > 2);

// console.log(expensiveProducts); // [{ name: 'Apple', price: 1.5 }, { name: 'Cherry', price: 2.0 }, { name: 'Durian', price: 5.0 }]

// // Example 2: Filtering an object based on property values
// /**
//  * In this example, we have an object representing a car. We want to get an array of property names that have string values. We use the Object.keys() method to get an array of property names, and then we use the filter() method to create a new array that only includes property names whose values are strings.
//  */

// const car = {
//   make: 'Honda',
//   model: 'Civic',
//   year: 2019,
//   color: 'blue',
// };

// // Filter object properties that have string values
// const stringProperties = Object.keys(car).filter(key => typeof car[key] === 'string');

// console.log(stringProperties); // ['make', 'model', 'color']

// //Example 3: Filtering an array of strings based on a condition
// /**
//  * In this example, we have an array of strings representing different words. We want to filter the array to only include words that have more than 5 characters. We use the filter() method with a callback function that checks the length property of each string.
//  */

// const words = ['apple', 'banana', 'cherry', 'durian', 'elderberry'];

// // Filter words that have more than 5 characters
// const longWords = words.filter(word => word.length > 5);

// console.log(longWords); // ['banana', 'cherry', 'elderberry']
