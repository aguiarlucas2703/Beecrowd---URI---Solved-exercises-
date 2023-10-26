#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
     double n;
    scanf("%lf", &n);
    n = n + 0.001;
    int nc = n / 100;
    double rc = fmod(n, 100);
    int ncq = rc / 50;
    rc = fmod(rc, 50);
    int nv = rc / 20;
    rc = fmod(rc, 20);
    int nd = rc / 10;
    rc = fmod(rc, 10);
    int ndc = rc / 5;
    rc = fmod(rc, 5);
    int ndd = rc / 2;
    rc = fmod(rc, 2);
    int num = rc / 1;
    rc = fmod(rc, 1);
    int mdc = rc / 0.50;
    rc = fmod(rc, 0.50);
    int mvc = rc / 0.25;
    rc = fmod(rc, 0.25);
    int mdd = rc / 0.10;
    rc = fmod(rc, 0.10);
    int mc = rc / 0.05;
    rc = fmod(rc, 0.05);
    int md1 = rc / 0.01;

    printf("NOTAS:\n");
    printf("%.0lf nota(s) de R$ 100.00\n", (double)nc);
    printf("%.0lf nota(s) de R$ 50.00\n", (double)ncq);
    printf("%.0lf nota(s) de R$ 20.00\n", (double)nv);
    printf("%.0lf nota(s) de R$ 10.00\n", (double)nd);
    printf("%.0lf nota(s) de R$ 5.00\n", (double)ndc);
    printf("%.0lf nota(s) de R$ 2.00\n", (double)ndd);

    printf("MOEDAS:\n");
    printf("%.0lf moeda(s) de R$ 1.00\n", (double)num);
    printf("%.0lf moeda(s) de R$ 0.50\n", (double)mdc);
    printf("%.0lf moeda(s) de R$ 0.25\n", (double)mvc);
    printf("%.0lf moeda(s) de R$ 0.10\n", (double)mdd);
    printf("%.0lf moeda(s) de R$ 0.05\n", (double)mc);
    printf("%.0lf moeda(s) de R$ 0.01\n", (double)md1);


  return(0);
}
