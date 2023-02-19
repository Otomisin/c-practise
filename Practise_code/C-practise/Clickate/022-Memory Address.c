/*
   // memory = an array of bytes within RAM (street)
   // memory block = a single unit (byte) within memory (house), used to hold some value (person)
   // memory address = the address of where a memory block is located (house address)
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h> //Variable for mathematical operations

int main (){
     char a = 'X';
     char b = 'Y';
     short c = 'Z';
     short d = 'A';
     int e = 'B';
     int f = 'C';
     double g = 'D';
     char h; //character
     char i[3]; // Array

     
     printf("%d Bytes\n", sizeof(a));
     printf("%d Bytes\n", sizeof(b));
     printf("%d Bytes\n", sizeof(c));
     printf("%d Bytes\n", sizeof(d));
     printf("%d Bytes\n", sizeof(e));
     printf("%d Bytes\n", sizeof(f));
     printf("%d Bytes\n", sizeof(g));
     printf("%d Bytes\n", sizeof(h));
     
     // To get the memory address. The format speciier is %p and & to get the adress     
     printf ("%p Address\n", &a);
     printf ("%p Address\n", &b);
     printf ("%p Address\n", &c);
     printf ("%p Address\n", &d);
     printf ("%p Address\n", &e);
     printf ("%p Address\n", &f);
     printf ("%p Address\n", &g);
     printf ("%p Address\n", &h);
     

     return 0;


}