/*
A function is a block of code which only runs when it is called. 
You can pass data, known as parameters, into a function.
Functions are used to perform certain actions, and they are important for reusing code: Define the code once, and use it many times.

Some examples of a function include: 
- main () which is used to execute code 
- printf () is used to output/print text to the screen


FUNCTION SYNTAX IN C

returnType functionName(parameter1, parameter2, parameter3) {
  // code to be executed
}

void myFunction() {
  // code to be executed
}

WHhere;
     -myFunction() is the name of the function
     -void means that the function does not have a return value. You will learn more about return values later in the next chapter
     -Inside the function (the body), add code that defines what the function should do

// https://www.w3schools.com/c/c_functions_parameters.php
*/

// #include <stdio.h>

// int main() {
//   printf("Hello World!\n");
//   return 0;
// }

// HOW TO CREATE A FUNCTION IN C 
void myfunction(){
     printf ("This just got executed\n");
}

// Call a function
// int main() {
//   myfunction(); // call the function
//   myfunction();
//   myfunction();
//   return 0;
// }

// PARAMETERS AND ARGUMENTS
// In this example, name is the parameter while "Tosin" is the argument
void myfunc(char name []){
     printf ("Hello %s\n", name );

}
//cal the function, myfunc
int main (){
     myfunc("Tosin");
     return 0;
}


// Passing Multiple parameter... character and integers

void name_func (char fname[], int age){
     printf ("Hello, your first name is %s and you are %d years old \n", fname, age );
}

int main (){
     name_func("Oluwatosin", 34);
     name_func("Totin", 23);
     name_func("Bolu", 22);
}

// Passing arrays as functioin parameters

void array_func ( int num[5]){
     for (int i = 0; i < 5; i++){
     printf ("%d\n", num[i]);
     }
     }

int main(){
     int num[5] = {12,22,12,33,21};
     array_func(num);
     return 0;
}

