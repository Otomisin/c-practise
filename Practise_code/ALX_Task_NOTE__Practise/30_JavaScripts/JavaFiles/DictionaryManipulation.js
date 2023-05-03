'use sctrict';

//// HOW TO MANIPULATE DICTIONARY IN JAVASCRIPTS /////////////////////
// Accessing the variables
let person = {name: "Tosin", age: 23, class : "grade 5"};
console.log(`The name is: ${person.name} from Nigeria and in class ${person.class}`)
console.log("The age is:" + person.age)

// Updating or adding to the varables
person.age = 30; // updating property
person.city = "Lagos"; // add property
person["Occupation"] = "'Senior Data, GIS and Vizualization Fellow'" //updating property
person.workPlace = "IOM"
console.log(person);

console.log(`The new age of ${person.name} is ${person.age} and he now lives in ${person.city} and works as a ${person.Occupation} with ${person.workPlace}`);

// Removing properties
delete person.workPlace; // removes the property
console.log(person);

// looping through properties;
for (let prop in person) {
  console.log(prop + ": " + person[prop]);
}

// checking id a property exist
console.log("name" in person); // true
console.log(person.hasOwnProperty("car")); // false