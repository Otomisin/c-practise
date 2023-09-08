let myPromise = new Promise((resolve, reject) => {
  let condition = true;

  if (condition) {
    resolve('Promise is resolved');
  } else {
    reject('Promise is rejected');
  }
});

// // Consuming a Promise ========
/**
 * Ue then and catch or use async/await that follow
 */
// myPromise
//   .then((message) => {
//     console.log('Success:', message);
//   })
//   .catch((message) => {
//     console.log('Failure:', message);
//   });

  // using async/await:
  async function handlePromise() {
    try {
      const message = await myPromise;
      console.log('Success:', message);
    } catch (error) {
      console.log('Failure:', error);
    }
  }
  
  handlePromise();
  
