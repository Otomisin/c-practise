/*
 If and Else 
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main  (){

     int age;
     printf("What is your age?");
     scanf ("%d", &age);

     if (age >= 18){
          printf("Congratulatioins you can register");
     }
     return 0;
}