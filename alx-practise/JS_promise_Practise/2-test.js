function double(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(value * 2);
    }, 1000);
  });
}

double(5)
  .then((result) => {
    return double(result);
  })
  .then((result) => {
    return double(result);
  })
  .then((result) => {
    console.log(result); // Output will be 40 (5 * 2 * 2 * 2)
  });


const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values); // Output: [3, 42, "foo"]
});
