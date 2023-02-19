/*
Variable is an allocated space in c
*/

#include <stdio.h> //LIbrary for standard input and output
#include <stdlib.h> //exit library


int main (){
     int x ; //declaration
     x = 123;

     int y = 456; // Declaration and initialization

     //variables
     int age = 21;                       //integer
     float gpa = 3.45;                   //floating point number
     char grade = 'B' ;                  //Single character
     char name[] = "Tosin Orenaike";    //Array of character

     //Format specifier
     printf("Hello %s\n", name);        //format specifer for character array
     printf("Your fake age is %d\n", age); //format specifier for integers
     printf("Your gpa is %f\n", gpa);   //format specifier for floating
     printf("Your fake grade is %c\n", grade); //format specifier for 

     //  make them show together
     printf("My name is %s. I am %d years old. My CGPA is %f and my grade is %c", name, age, gpa, grade);

     return 0;
}
