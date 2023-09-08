const redis = require('redis');
const client = redis.createClient(6379, 'localhost');

client.on('connect', function() {
    console.log('Connected to Redis');
});

client.on('error', function(err) {
    console.log('Redis error: ' + err);
});

// SET operation
client.set('key', 'value', redis.print);  // Output will be "Reply: OK"

// GET operation
client.get('key', function(err, reply) {
    console.log(reply);  // Will print the value for 'key'
});

// // DEL operation
// client.del('key', function(err, reply) {
//     console.log(reply);  // Will print '1' if the key existed, or '0' if it did not
// });


// How to store has values =============================
// HSET operation
client.hset('user:1', 'name', 'John', redis.print);  // Output will be "Reply: 1"

// HGET operation
client.hget('user:1', 'name', function(err, reply) {
    console.log(reply);  // Will print 'John'
});
