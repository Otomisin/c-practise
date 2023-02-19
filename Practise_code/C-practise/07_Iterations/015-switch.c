/*
 Switch statment
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     char grade;

     printf ("Please enter a letter grade: ");
     scanf ("%c", &grade);

     switch (grade){
     case 'A':
          printf("Wow you scored an A");
          break;
     case 'B':
          printf("Wow you scored an B");
          break;
     case 'C':
          printf("Wow you scored an C");
          break; 
     case 'D':
          printf("Wow you scored an D");
          break;
     case 'E':
          printf("Wow you scored an E");
          break;
     case 'F':
          printf("Wow you scored an F");
          break;
     default:
          printf("Enter a valide grade");         
                    
     }

     return 0;
}