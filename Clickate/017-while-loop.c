/*
    // while loop = repeats a section of code possibly unlimited times. 
    // WHILE some condition remains true
    // a while loop might not execute at all
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     int i = 1;
     while (i <= 20)     
     {
          printf("Number %d\n", i);
          i++;
     }
      

     return 0;
}