/**
*The conditions below is initializing multiple test conditions
*1. It is initializing two variables. Note: both are separated by * comma (,).
*2. It has two test conditions joined together using AND (&&) logical operator. Note: You cannot *use multiple test conditions separated by comma, you must use logical operator such as && or || *to join conditions.
*3. It has two variables in increment part. Note: Should be separated by comma
 */

#include <stdio.h>
int main()
{
   int i,j;
   for (i=1,j=5 ; i<3 || j<10; i++,j++)
   {
	printf("%d, %d\n",i ,j);
   }
   return 0;
}