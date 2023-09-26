#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  double n, pi, v;

  pi = 3.14159;

  scanf("%lf", &n);

  v = (4/3.0) * pi * pow(n, 3);

  printf("VOLUME = %.3lf\n", v);

  return(0);
}
