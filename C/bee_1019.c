#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int n, h, r, s, minu;

  scanf("%d", &n);

  h = n / 3600;
  r = n % 3600;
  minu = r / 60;
  s = r % 60;

  printf("%d:%d:%d\n", h, minu, s);


  return(0);
}
