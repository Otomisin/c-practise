/*
    // Continue => skips the rest of the code and force the next iteratioin of the loop
    // Break => exist aloop/switch
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     
     int i;
     for (int i = 1; i <= 20; i++){
          if (i == 7){
               continue;
               //break;
          }
          printf("%d\n", i);
     }
     return 0;


}