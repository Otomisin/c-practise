//the simplest fetch you can use and still have error handling
const url = 'https://jsonplaceholder.typicode.com/users';

//fetching the users from json placeholder api
export async function getDat(){
  let response = await fetch(url);
  console.log(response);
  let dataObj = await response.json();
  console.log(dataObj);
}