/*
   //Multi-Dimentsional array = a data structure that can store many values of the same data type
   2D array = an array, where each element is an entire array
   //            useful if you need a matrix, grid, or table of data
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Function for mathematical operations


int main (){

     int numbers [2][5] = {{1,2,3,4,5},{6,7,8,9,10}};
     // printf("%d", numbers[1][2]);


     //To avoid having to always change the loops when a new row or col is added, you can use this method
     //int numbers [2][3];
     int rows = sizeof(numbers)/sizeof(numbers[0]);
     int columns = sizeof (numbers[0]) / sizeof (numbers [0][0]);

          // Loop through the whole table
     for (int r = 0; r < rows;  r++ ){
          for (int c = 0; c < columns; c++){
               printf( " %d ", numbers[r][c]);
          }
          printf("\n");
     }

     return 0;


}