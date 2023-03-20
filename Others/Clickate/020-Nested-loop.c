/*
    // Nested loop creates a loop within another loop
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     int i, j;
     for (i = 1; 1 <= 3; i++){
          printf("This is the outer loop starting %d\n", i);
               for (j = 1; j <= 4; j++){
                    printf("      This is the inner loop %d \n", j);
               }
          printf ("This is the outer loop %d ending\n", i);
          //break;
     }


     return 0;    


}