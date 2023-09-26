#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main ()
{
  int a, b, c, d, r;

  scanf("%d", &a);
  scanf("%d", &b);
  scanf("%d", &c);
  scanf("%d", &d);

  r = (a * b - c * d);
  printf("DIFERENCA = %d", r);

  return(0);
}
