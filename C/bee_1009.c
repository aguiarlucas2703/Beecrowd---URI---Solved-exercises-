#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  char nome[100];
  double s, v, t;

  scanf("%s", &nome);
  scanf("%lf", &s);
  scanf("%lf", &v);

  t = (0.15 * v)  + s;

  printf("TOTAL = R$ %.2lf\n", t);



  return(0);
}
