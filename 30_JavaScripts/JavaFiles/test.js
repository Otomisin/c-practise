const products = [
  { name: 'Apple', price: 1.5 },
  { name: 'Banana', price: 0.5 },
  { name: 'Cherry', price: 2.0 },
  { name: 'Durian', price: 5.0 },
];

console.log(typeof(products));

// Filter products that cost more than $1
const expensiveProducts = products.filter(product => product.price > 2);

console.log(expensiveProducts); // [{ name: 'Apple', price: 1.5 }, { name: 'Cherry', price: 2.0 }, { name: 'Durian', price: 5.0 }]
