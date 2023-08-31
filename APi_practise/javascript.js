//the simplest fetch you can use and still have error handling
const url = 'https://jsonplaceholder.typicode.com/users';

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(dataObj => {
        console.log(dataObj);
    })
    .catch(error => {
        console.log('There was a problem with the fetch operation:', error.message);
    });