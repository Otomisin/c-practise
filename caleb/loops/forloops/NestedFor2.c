#include <stdio.h>

int main ()
{
     for (int i = 0 ; i < 2; i++)
     {
          for (int j = 0; j < 2; j++)
          {
               for (int k = 0 ; k < 2; k++)
               {
                    printf("%d, %d, %d\n", i, j, k);
               }
               
          }
     }
     return 0;
}