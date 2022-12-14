/*
Augmented assignement operators is used to replace a statement where an operator takes a varaible as one of it's arguments and then assigne the result back to the same variable. For example 
x= x+1
x+ =1

*/

#include <stdio.h>
#include <string.h>

int main (){
     int x = 10;

     // x = x + 2;
     // x+=2;

     // x = x - 2
     //x-=2;

     // x = x * 2;
     //x*=2;

     // x = x % 2;
     x%=2;

     printf("The result is: %d", x);
     
     return 0;
}