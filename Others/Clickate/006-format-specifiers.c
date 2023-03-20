/*
Format specifiers
*/

#include <stdio.h> //LIbrary for standard input and output
#include <stdlib.h> //exit library
#include <stdbool.h> //needed for using boolean


int main (){
        // format specifier % = They are used within a printf statement. Its defines and formats a type of data to be displayed

    // %c = character
    // %s = string (array of characters) 
    // %f = float
    // %lf = double
    // %d = integer

    // %.1 = decimal precision
    // %1 = minimum field width
    // %- = left align


    float shoe = 10.78;
    float bag = 120.78;
    float shirt = 3810.78;

    printf("The shoe costs : $%8.2f\n", shoe); //8 is for field width and .2 is for the decimal places
    printf("The bag costs : $%10.3f\n", bag);     //10 is for field width and .3 is for the decimal places
    printf("The shirt costs : $%-9.2f", shirt);   //-9 is for field width to the left  and .2 is for the decimal places
    
     
 return 0;
}
