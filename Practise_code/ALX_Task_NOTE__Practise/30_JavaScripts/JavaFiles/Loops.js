'use strict'; // Helpd to get the correct output

let country = "Nigeria"
let continent = "Africa"

console.log(country)
console.log(continent)

///////////////////////////////////////////////
// SWITCH
const day = 'Friday';

switch (day) {
  case 'monday':
    console.log('Today is monday, go to office');
    console.log('Today is monday, go jogging');
    break;
  case 'Tuesday':
    console.log('Today is Tuesday, go to the gym');
    console.log('Today is Tuesday, cook');
    break;
  case 'Wednesday':
  default:
    console.log('Not a noteable date')  
}

// USING IF
if (day === 'monday'){
  console.log('Today is monday, go to office');
  console.log('Today is monday, go jogging');
} else if (day === 'tuesday'){
  console.log('Today is Tuesday, go to the gym');
  console.log('Today is Tuesday, cook');
} else if (day === 'Friday'){
  console.log('Today is friday, you have weekly meeting')
} else {
  console.log('Not a valid date')}

let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true;
if (hasDriversLicense) console.log('I have a drives')


// While Loop
let i = 1;
while (i <=5){
  console.log(i);
  i++
}

// For Loop
for (let i = 1; i <= 5 ; i++){
  console.log(i);
}