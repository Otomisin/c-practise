/*
   // array = a data structure that can store many values of the same data type
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Function for mathematical operations


int main (){
   //int prices [] = {23.0, 25.0, 53.0, 96.0, 63.0, 23.0, 25.0, 53.0, 96.0, 63.0}; //Setting up an array
   double prices [] = {23.0, 25.0, 53.0, 96.0, 63.0, 23.0, 25.0, 53.0, 96.0, 63.0}; //Setting up an array | use double to intialize since it's a figure with decimal

   printf("Price is: %.2lf\n", prices[0]); //the format specifier for decimals is lf. Use 2 to set the decimal place. You call out an array based on the index valu. 
   printf("Price is: %.2lf\n", prices[1]);
   printf("Price is: %.2lf\n", prices[2]);
   printf("Price is: %.2lf\n", prices[3]);
   printf("Price is: %.2lf\n", prices[4]);

   //alternatively you can loop through array
   for (int i = 0; i < sizeof(prices)/sizeof(prices[0]); i++){
      printf("Price is: $%.2lf\n", prices[i]);
   }
     return 0;


}