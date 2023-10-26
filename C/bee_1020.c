#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int ano, r, m, d, ent;

  scanf("%d", &ent);
  ano = ent / 365;
  r = ent % 365;
  m = r / 30;
  d = r % 30;

  printf("%d ano(s)\n", ano);
  printf("%d mes(es)\n", m);
  printf("%d dia(s)\n", d);

  return(0);
}
