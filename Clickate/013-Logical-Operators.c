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

     if (x < 40 && alpha =='B'&& sunny == true){ // True can also be set to 1 and used alone as "sunny"
     printf("The AND condition is trie");
} else {
     printf("This condition is not meet");
}     
     return 0;
}