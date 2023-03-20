/*
    // BITWISE OPERATORS = special operators used in bit level programming

    //MY Note: 
    Bitwise operators are used to change individual bits in an operand. A single byte of computer memory-when viewed as 8 bits-can signify the true/false status of 8 flags because each bit can be used as a boolean variable that can hold one of two values: true or false.

    The bitwise operators are similar to the logical operators, except that they work on a smaller scale -- binary representations of data
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     int x = 6; // 6 =
     int y = 12; //
     int z = 0; //

     z = x & y;
     printf("AND is %d\n", z);

     z = x | y;
     printf("OR is %d\n", z);

     z = x ^ y;
     printf("XOR is %d\n", z);

     z = x << 2;
     printf ("shift left is %d\n", z);

     z = x << 2;
     printf ("right left is %d\n", z);



     return 0;
}