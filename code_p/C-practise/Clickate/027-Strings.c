/*
   //String Array in C Language Programming
*/

#include <stdio.h>
#include <string.h> //for strings 
#include <stdbool.h>
#include <math.h> //Function for mathematical operations


int main (){
     char cars [][10] = {"Mustang", "Corvete","Camaro"};

     strcpy(cars[0],"Tesla"); // strcpy() is a standard library function in C/C++ and is used to copy one string to another
     for (int i = 0; i < sizeof(cars)/sizeof(cars[0]); i++){
          printf("%s\n", cars[i]);
     }

  return 0;

     }

   
