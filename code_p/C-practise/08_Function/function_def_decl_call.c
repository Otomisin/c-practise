#include <stdio.h>

void sum(); // function declaratioin

void main ()
{
	sum (); // function calling
}

void sum () // functioin definition
{
  int a, b, sum =0;
  printf ("enter two number: ");
  scanf ("%d%d", &a, &b);
  sum = a+b;
  printf ("sum = %d\n", sum);
}

// // FLOATS
// float sum(); // function declaratioin

// void main ()
// {
// 	sum (); // function calling
// }

// float sum () // functioin definition
// {
//   float a, b, sum =0;
//   printf ("enter two number: ");
//   scanf ("%f%f", &a, &b);
//   sum = a+b;
//   printf ("sum = %f\n", sum);
// }