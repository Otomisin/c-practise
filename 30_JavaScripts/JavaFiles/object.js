const fruits = ["Banana", "Orange", "Apple", "Mango"];
const fruit = Object.keys(fruits);
console.log(Object.keys(fruit));

const myObj = { 
  name: 'John', 
  age: 30, 
  address: '123 Main St' 
};

// Uisng Object.keys to get keys
const key = Object.keys(myObj);
console.log(key);

// Uisng Object.keys to get keys
const values = Object.values(myObj);
console.log(values);

// Using object.entries to retrieve the key-value pair
// const entry = Object.entries(myObj);
console.log(Object.entries(myObj));
