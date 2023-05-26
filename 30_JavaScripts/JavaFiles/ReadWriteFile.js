////////////////////////////////////////
// Reading files using the fs
////////////////////////////////////////////

// const fs = require('fs');
// const path = './sample.txt' //define the path to the file/

// fs.readFile(path, 'utf-8', function(error,
//   data) {
//     if(error){
//       console.log(error);
//   } else {
//     console.log(data);
//   }
// });

// or the promised-based syntax method ////////////

// const fs = require('fs').promises;

// fs.readFile('sample.txt')
//   .then((data) => {
//     console.log(data.toString());
//   })
//   .catch((err) => {
//     console.error(err);
//   });

//////////////////////////////////
// To write a file ///////////////
//////////////////////////////

// const fs = require('fs');
// const data = 'Hello, world'; // Data to write

// fs.writeFile('./n_Sample.txt', data, (err) => {
//   if (err) {
//     console.log(err);
//     return;
// }
//   console.log('file has been written!');
// });

// or using the promised based

const fs = require('fs').promises;
const file = 'Hello, world'; // Data to write
fs.writeFile('./p_file', file )
  .then(() => {
    console.log('file has been written!');
    
  }).catch((err) => {
    console.error(err);
  });

