#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main()
{
  int a, b, c, d, v;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  v = 0;
  if (b > c & d > a & c + d > a + b){
      v = 1;
  }
  if (c > 0 % d > 0 & a % 2 == 0){
      v = v + 1;
  }

  if (v == 2){
    printf("Valores aceitos\n");
  }

  else{
     printf("Valores nao aceitos\n");
  }

  return(0);
}
