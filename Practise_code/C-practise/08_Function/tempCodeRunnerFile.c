float sum(); // function declaratioin

void main ()
{
	sum (); // function calling
}

float sum () // functioin definition
{
  float a, b, sum =0;
  printf ("enter two number: ");
  scanf ("%f%f", &a, &b);
  sum = a+b;
  printf ("sum = %f\n", sum);
}