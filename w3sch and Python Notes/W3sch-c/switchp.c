#include <stdio.h>

int main (void) {
    int day = 6;

    switch (day)
    {
    case 1 /* constant-expression */:
        /* code */
        printf ("Monday\n");
        break;
    case 2:
        printf ("Tuesday\n");
        break;
    case 3:
      printf("Wednesday\n");
      break;
    case 4:
      printf("Thursday\n");
      break;
    case 5:
      printf("Friday\n");
      break;
    case 6:
      printf("Saturday\n");
      break;
    case 7:
      printf("Sunday\n");
      break;
    }
    return (0);
}