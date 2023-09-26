#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int a, b;
  double c;

  scanf("%d", &a);
  scanf("%d", &b);

  c = (a * b) / 12.0;

  printf("%.3lf\n", c);

  return(0);
}
