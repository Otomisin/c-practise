/*
Arithmetic Operator in C programming
The Arithmetic operators are some of the C Programming Operator, which are used to perform arithmetic operations includes operators like Addition, Subtraction, Multiplication, Division and Modulus.All these Arithmetic operators in C are binary operators which means they operate on two operands.

ARITHMETIC OPERATORS	OPERATION	EXAMPLE
+	Addition	10 + 2 = 12
–	Subtraction	10 – 2 = 8
*	Multiplication	10 * 2 = 20
/	Division	10 / 2 = 5
%	Modulus – It returns the remainder after the division	10 % 2 = 0 (Here remainder is zero). If it is 10 % 3 then it will be 1.
*/

#include<stdio.h>
int main()
{
    int a,b,c;
    float x;
    printf("\nEnter 2 Nos : ");
    scanf("%d%d",&a,&b);
    c=a+b;
    printf("\nTotal : %d",c);
    c=a-b;
    printf("\nDifference : %d",c);
    c=a*b;
    printf("\nMul : %d",c);
    x=(float)a/(float)b;
    printf("\nDiv : %0.2f",x);
    c=a%b;
    printf("\nMod : %d",c);
    return 0;
}