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

  // Object methods One
  lidOpen:false,
  toggleLid: function (lidStatus){
    this.lidOpen = lidStatus; //this refers to the current object
  },

  // Object methods two
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

////////////////////////////////////////////////
//Creating Object blueprints (Class)
////////////////////////////////////////////////
/**
 * Creating classes:
 *
 * Class declaration: class Name {}
 * Class expression:  const Name = class {}
 */

class Backpack {
  constructor(
    // Defines parameters:
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen
  ) {
    // Define properties:
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
  }
  // Add methods like normal functions:
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
}

export default Backpack;