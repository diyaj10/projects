#include <stdio.h>
#include <stdlib.h>

int main()
{
	char ch;
	double a, b;
	while (1) {
		printf("Enter an operator (+, -, *, /) \n");
		scanf(" %c", &ch);

		
		printf("Enter two first and second operand: ");
		scanf("%lf %lf", &a, &b);

		switch (ch) {

		
		case '+':
			printf("%.1lf + %.1lf = %.1lf\n", a, b, a + b);
			break;

		case '-':
			printf("%.1lf - %.1lf = %.1lf\n", a, b, a - b);
			break;

		case '*':
			printf("%.1lf * %.1lf = %.1lf\n", a, b, a * b);
			break;

		case '/':
			printf("%.1lf / %.1lf = %.1lf\n", a, b, a / b);
			break;

		default:
			printf(
				"Error! please write a valid operator\n");
		}

		printf("\n");
	}
}
