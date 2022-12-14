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

     else if (age >=0 && age < 18){
          printf("You are too young to bet");
     }

     else if (age < 0){
     printf("Kindly add a more reliable age");
     }     

     else {
          printf("Sorry,You can't register");
     }  

     return 0;
}