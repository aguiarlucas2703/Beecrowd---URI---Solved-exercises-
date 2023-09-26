#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  float a, b, c, d, p;

  scanf("%f %f", &a, &b);
  scanf("%f %f", &c, &d);

  p = sqrt(((c -a) * (c - a)) + ((d - b) * (d - b)));

  printf("%.4f\n", p);

  return(0);
}
