/**LINKS
 * https://www.udemy.com/course/the-complete-javascript-course/learn/lecture/* 2648255#overview
 * 
 */

'use strict'; // Helpd to get the correct output

// let country = "Nigeria"
// let continent = "Africa"

// console.log(country)
// console.log(continent)

///////////////////////////////////////////////
// // SWITCH
// const day = 'Friday';

// switch (day) {
//   case 'monday':
//     console.log('Today is monday, go to office');
//     console.log('Today is monday, go jogging');
//     break;
//   case 'Tuesday':
//     console.log('Today is Tuesday, go to the gym');
//     console.log('Today is Tuesday, cook');
//     break;
//   case 'Wednesday':
//   default:
//     console.log('Not a noteable date')  
// }


// if (day === 'monday'){
//   console.log('Today is monday, go to office');
//   console.log('Today is monday, go jogging');
// } else if (day === 'tuesday'){
//   console.log('Today is Tuesday, go to the gym');
//   console.log('Today is Tuesday, cook');
// } else if (day === 'Friday'){
//   console.log('Today is friday, you have weekly meeting')
// } else {
//   console.log('Not a valid date')

// let hasDriversLicense = false;
// const passTest = true;

// if (passTest) hasDriversLicense = true;
// if (hasDriversLicense) console.log('I have a drives')

// ARRAYS /////////////////////////////////////////////////////
// Method 1: creating an array 
const friend1 = 'Michael';
const friend2 = 'Steven';
const friend3 = 'Peter';

const friend = ['Micheal','Steven','Peter'];
console.log(friend);

// Method 2: creating an array
const family = new Array('Tosin','Bola', 'Segun');
console.log(family[0]); // Accesing arrays
console.log(family[1]); // Accesing the second elements in an arrays
console.log(family.length); // Accesing the lenght of an arrays
console.log(family[family.length-1]); // Accesing last arrays

family[1] = 'Lola' // Changing array values
console.log(family)


//// OBJECTS////////////////////////////////////////////
// This is what an object looks like in Javascript

const backpack = {
  // Object Properties
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLenght: {
    left:26,
    right: 26,
  },
  lidOpen:false,
  // Object methods
  lidOpen:false,
  toggleLid: function (lidStatus){
    this.lidOpen = lidStatus; //this refers to the current object
  },
  newStrapLength: function (lenghtLeft, lenghtRight){
    this.strapLenght.left = lenghtLeft,
    this.strapLenght.right = lenghtRight;
  },
};

console.log(backpack)
/** There are two ways of accessing object propertise,
 * individual propertise and methods within that object 
 * There is bracket notation and dot notation
 */

//Dot notation method of accessing object properties
console.log("The backpack object:",backpack);
console.log("The value of the pocket numberis: ",backpack.pocketNum);
console.log("The strap left L: ", backpack.strapLenght.left);

// Bracket notation method of accessing object properties
console.log("The value of the pocket number using bracket notation is: ",backpack["pocketNum"]); // this is helpful for parsing and using vraiables in the bracket notation as in the examples below
var query = 'pocketNum';
console.log("The pocketNum value using variable bracket notation: ", backpack[query])

// Accessing and using object methods
backpack.newStrapLength(10, 25); // Using the method newStrapLenght
console.log(backpack.strapLenght) // Out putting the new newStrapLenght

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
console.log(person.hasOwnProperty("car"));