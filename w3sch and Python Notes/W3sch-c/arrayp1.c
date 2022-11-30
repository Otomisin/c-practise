#include <stdio.h>

int main (void)

{
    int myNumber []= {25, 50, 75, 100};
    int i;

    for (i = 0; i < 4; i++){
        printf("%d\n", myNumber[i]);
    }
    return (0);
}