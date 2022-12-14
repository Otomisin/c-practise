/*
   //A function prototype is a declaration in the code that instructs the compiler about the data type of the function, arguments and parameter list.

*/

#include <stdio.h>
#include <string.h> //for strings 
#include <stdbool.h>
#include <math.h> //Function for mathematical operations

void greeting(char name [], int age); // the function prototype here in is the char [] and int age parameters

int main() {
   greeting ("Tosin", 70); //the arguments here are hte Tosin and 70
   return 0;
}

void greeting (char name [], int age){
   printf ("Hello %s, You are welcome \n", name);
   printf ("You are %d years old\n", age);

}