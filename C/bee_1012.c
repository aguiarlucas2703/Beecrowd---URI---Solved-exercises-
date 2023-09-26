#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  double a, b, c, a1, a2, a3, a4, a5, pi;

  pi = 3.14159;

  scanf("%lf %lf %lf", &a, &b, &c);

  a1 = (a * c) / 2;
  a2 = pi * (c * c );
  a3 = ((a + b) * c) / 2;
  a4 = b * b;
  a5 = a * b;

  printf("TRIANGULO: %.3lf\n", a1);
  printf("CIRCULO: %.3lf\n", a2);
  printf("TRAPEZIO: %.3lf\n", a3);
  printf("QUADRADO: %.3lf\n", a4);
  printf("RETANGULO: %.3lf\n", a5);



  return(0);
}
