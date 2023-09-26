#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int n, nc, rc, ncq, rcq, nv, rv, nd, rd, ndc, rdc, ndd, rdd, nu;

  scanf("%d", &n);

  nc = n / 100;
  rc = n % 100;
  ncq = rc / 50;
  rcq = rc % 50;
  nv = rcq / 20;
  rv = rcq % 20;
  nd = rv / 10;
  rd = rv % 10;
  ndc = rd / 5;
  rdc = rd % 5;
  ndd = rdc / 2;
  rdd = rdc % 2;
  nu = rdd / 1;

  printf("%d\n", n);
  printf("%d nota(s) de R$ 100,00\n", nc);
  printf("%d nota(s) de R$ 50,00\n", ncq);
  printf("%d nota(s) de R$ 20,00\n", nv);
  printf("%d nota(s) de R$ 10,00\n", nd);
  printf("%d nota(s) de R$ 5,00\n", ndc);
  printf("%d nota(s) de R$ 2,00\n", ndd);
  printf("%d nota(s) de R$ 1,00\n", nu);


  return(0);
}
