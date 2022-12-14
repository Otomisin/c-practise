/*
 Mathematical Operatioins
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main  (){
     int A = round(7.146);
     int B = ceil(4.146); // Round up
     int C = floor (3.99); //Round Down
     double D = sqrt (9); //Square root
     double E = pow(2, 4); //Raise to power
     double F = fabs(-100); //Absolute from 0
     double G = log (3);


     printf ("The result %d\n", A);
     printf ("The result %d\n", B);
     printf ("The result %d\n", C);
     printf ("The result %lf\n", D);
     printf ("The result %lf\n", E);
     printf ("The result %lf\n", F);
     printf ("The result %lf\n", G);
     
     return 0;
}