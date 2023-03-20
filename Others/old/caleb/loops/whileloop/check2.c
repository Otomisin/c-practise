#include <stdio.h>

int main  (void)
{
     int i = 1, k = 3;
     while (i <= 4 || k <= 5)
     {
          printf ("%d  %d \n", k, i);
          i++;
          k++;
     }

     return 0;     

}