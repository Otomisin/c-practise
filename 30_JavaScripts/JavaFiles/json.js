/////////////////////
// Parsing JSON Data
/////////////////////
/**
 * Use the JavaScript function JSON.parse() to convert text into a JavaScript object:
 */

person_str = '{"name":"John", "age":30, "city":"New York"}'
console.log(typeof(person_str)); //String

const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}')
console.log(typeof(obj)); //object

//////////////////////////////////
// Stringifying JavaScript Objects
//////////////////////////////////
/**
 * To convert a JavaScript object into a JSON string, use the JSON.`stringify()` method. 
 */

const person2 = { name: "Tolu", age: 30, city: "New York" };
const jsonString = JSON.stringify(person2);
console.log(typeof(jsonString));

////////////////////////////
// Acccessing JSON DATA
///////////////////////////
/**
 * To access the data in a JavaScript object that was created from a JSON string, use the dot notation or bracket notation. For example: * 
 */
person = {name: 'Tosin', age:20, city: 'Lagos'}
console.log(typeof(person));
console.log(person.city);
console.log(person["name"]);

//////////////////////////////
// Modifying JSON Data
//////////////////////////////
/**
* To modify the data in a JavaScript object that was created from a JSON * string, simply access the property and assign a new value to it. For * * example
*/

const jsonStringn = '{"name":"John", "age":30, "city":"New York"}';
const objn = JSON.parse(jsonStringn);

objn.age = 35;
console.log(objn.age); // Output: 35

objn.gender = "Male";
console.log(objn); //// Output: {name: "John", age: 30, city: "New York", gender: "Male"}


