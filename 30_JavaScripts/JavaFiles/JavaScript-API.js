 /**
  * 
  * In this example, **`fetch()`** is used to send a GET request to the URL **`'https://api.example.com/data'`**. The **`then()`** method is used to handle the response when it is received. In this case, the **`response`** object is converted to JSON using the **`json()`** method, and then the resulting data is logged to the console using **`console.log()`**. If an error occurs, it is caught using the **`catch()`** method and logged to the console using **`console.error()`**.
  */
////////////////////////////////////////////////////////
 //example of sending an API request using fetch():
 /////////////////////////////

// fetch('https://jsonplaceholder.typicode.com/users/1')
//  .then(response => response.json())
//  .then(data => console.log(data))
//  .catch(error => console.error(error))


//////////////////////////////////////////////////////
 // example of sending an API request with additional options using fetch():
 /////////////////////////////

// const options = {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json'
//   },
//   body: JSON.stringify({
//     name: 'John Doe',
//     username: 'johndoe',
//     email: 'johndoe@example.com'
//   })
// };

// fetch('https://jsonplaceholder.typicode.com/users/', options)
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(error => console.error(error));
