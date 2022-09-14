#include <stdio.h>

int main (void)

{
    int time = 22;
    if (time< 10){
        printf ("Good morning.");
    } else if (time> 10) {
        printf ("Good day. ");
    } else  {
        printf("Good Evening. " );
    }
    return (0);
}