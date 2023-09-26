#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main ()
{
  double r, a, pi;


  pi = 3.14159;
  scanf("%lf", &r);
  a = pi* (r*r);


  printf("A=%.4lf", a);

  return(0);
}
