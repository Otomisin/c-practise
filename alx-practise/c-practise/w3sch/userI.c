#include <stdio.h>

int main (void){
    // Creates a string
    char firstname [30];

    //Ask for the their names
    printf ("Enter your first name: \n");

    //Get the asked name
    scanf ("%s", firstname);

    //Output the name
    printf ("Hello %s\n", firstname);

    return 0;
}