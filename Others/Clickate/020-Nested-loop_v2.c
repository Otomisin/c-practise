/*
    // Nested loop creates a loop within another loop
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     int i, j;

    for (i = 1; i = 3; i++) {
        printf("This is the outer loop %d starting\n", i);
            for(j = 1; j = 4; j++){
                printf("        This is the inner loop %d\n", j);
            }
        printf("This is the outer loop %d ending\n", i);
    }


    return 0;   


}