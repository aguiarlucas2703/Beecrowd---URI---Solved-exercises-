#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int cod, uni, cod2, uni2;
  float pre,pre2, t;

  scanf("%d %d %f", &cod, &uni, &pre);
  scanf("%d %d %f", &cod2, &uni2, &pre2);

  t = uni * pre + uni2 * pre2;

  printf("VALOR A PAGAR = R$ %.2f", t);

  return(0);
}
