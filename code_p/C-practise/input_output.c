/*
Input and output: https://www.youtube.com/watch?v=FwpP_MsZWnU&ab_channel=JonathanEngelsma

-scanf() function take the user input 
-printf() function to display output to the user.

*/
#include <stdio.h>

int main (void)
{
     printf ("Hello Mr Man\n");
     printf ("Who: %s size: %d cost: %0.3f'\n", "you", 12, 1.2);
     printf ("Your initials are %c%c%c and your age is %d\n", 'O', 'T', 'O',29);

     // Using standard input scanf()
     
     char f, m , l;
     int age;
     printf ("Enter your initials and then age: ");
     scanf ("%c %c %c %d", &f, &m, &l, &age);
     printf ("Your initials are %c%c%c and your age is %d\n", f, m,l, age);
}

