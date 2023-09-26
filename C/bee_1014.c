#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int x;
  float y, m;

  scanf("%d", &x);
  scanf("%f", &y);

  m = x / y;

  printf("%.3f km/l\n", m);


  return(0);
}
