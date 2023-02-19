/*
   //String Array in C Language Programming
*/

#include <stdio.h>
#include <string.h> //for strings 
#include <stdbool.h>
#include <math.h> //Function for mathematical operations


int main (){
     char string1[] = "Tosin";
     char string2[] = "Orenaike";

     // strlwr (string1);        //converts a string to lowercase
     // strupr (string2);        // convert a string to upper case
     // strcat (string1, string2);      //Appends string2  to end of string 1
     // strncat (string1, string2, 3);     //aapends n characters from strings to string1
     // strccpy (string1, string2);        //copy strings2 to string1
     // strncpy (string1, string2, 3);     //copy n chracters of string2 to string1

     // strset(string1, '?');    //sets all chracters of a string to a given character
     // strnset (string1,'x', s);          //sets the first n chracter of a string to a given character
     // strrev (string1);        //reverse a string

     // printf ("%s", string1);

     // int result = strlen(string1); //This returns the length of the string
     int result = strcmp (string1, string2); //string compare all characters
     int result = strncmp(string1, string2, 1); // This compares n chracter

     printf("%d", result);      


  return 0;

     }

   
