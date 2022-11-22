/*
User input
*/

#include <stdio.h>
#include <string.h>

int main(){

    int age;
    char name[40];

// Name input 
    printf("what is your name?");
    scanf("%s", name); //No need for the hamper sign (&) for strings. To collect an input with a space in them, such as a first and second name you use fget
    fgets(name, 40, stdin); // To collect an input with a space in them, such as a first and second name you use fget

// age input
    printf ("How old are you: ");
    scanf  ("%d", &age); //There is a need to add hamper signe for integers, in this case &age

    printf("How are you %s\n", name);
    printf("You are %d years old", age );
    

    return 0;
}