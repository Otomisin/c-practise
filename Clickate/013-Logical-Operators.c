/*
 Logicl Operators
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main (){

     // Logical Operators
     // && AND
     // 
     int x = 25;
     char alpha = 'B';
     bool sunny = true;
/*

// Ussing &&
if (x < 40 && alpha =='B'&& sunny == true){ // True can also be set to 1 and used alone as "sunny"
     printf("The AND condition is trie");
} else {
     printf("This condition is not meet");
} 

*/   

// /*Using or 
/*
if (x < 40 || alpha =='B'|| sunny == true){ // True can also be set to 1 and used alone as "sunny"
     printf("The AND condition is true");
} else {
     printf("This condition is not meet");
} 
*/

// Using not; ! ||
if (!sunny){ // True can also be set to 1 and used alone as "sunny"
     printf("It is cloudy");
} else {
     printf("It is sunny");
} 
     return 0;
}