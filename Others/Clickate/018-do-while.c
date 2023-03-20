/*
    // do while loop = always executes a block of code once, THEN checks a condition
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     int i = 1;
     do {
          printf("Number %d\n", i);
          i++;
     } while (i <=20);
      

     return 0;
}