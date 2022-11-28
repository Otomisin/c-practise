/*
   // pointer = a "variable-like" reference that holds a memory address to another variable, array, etc.
   //           some tasks are performed more easily with pointers
   //           * = indirection operator (value at address)
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

//Create a printage function
void printage (int age){
printf("You are %d Years old", age);
}
   

int main (){
     int age = 25;
     int *ptr_age = &age;  //this stores the address of age

     printf ("LEFT SIDE is the ADDRESS %p\n", &age);
     printf ("RIGHT SIDE is value %p\n", &age);
     printf("Address of pointer = %p\n", &ptr_age);

     printf ("The value of the pointer age = %p\n", ptr_age);
     printf("Value at the memory address of ptr_age is %d\n", *ptr_age); //derefrencing
     
     //checking the size of the variable age and ptr_age
     printf("The size of the variable age %d\n", sizeof(age));
     printf ("The size of the pointer ptr_age is %d \n", sizeof(ptr_age));

     printage(30); //Call the function printage function

     return 0;


}