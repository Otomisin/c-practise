#include <stdio.h>

int main (void)

{
    int time;
    printf("what is the time? ");
    scanf("%i", &time);

    if (time < "%i"){
        printf ("Good morning.");
    } else if (time > "%i"){
        printf ("Good day. ");
    } else  {
        printf("Good Evening. " );
    }
    return (0);
}