#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main ()
{
  int n, h;
  float v, s;

  scanf("%d", &n);
  scanf("%d", &h);
  scanf("%f", &v);

  s = h * v;

  printf("NUMBER = %d\nSALARY = U$ %.2f\n", n, s);



  return(0);
}
