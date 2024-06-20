#include <stdio.h>
#include <math.h>

void save_binary(int val, int n, int *save) {
  int i, tmp;
  int value, rest;
  

  value = val;
  for (i=n - 1; i>-1; i--) {
    tmp = pow(10, i);
    *save++ = value / tmp;
    printf("[%d, %d] %d\n", value, tmp, value / tmp);
    value %= tmp;
  }
}

int main(int argc, char **argv)
{
  int i, n, val, rest, a;
  int tmp;
  int ary[50];
  printf("Hello world\n");

  scanf("%d", &n);
  scanf("%d", &tmp);

  printf("n: %d\n", n);
  printf("tmp: %d\n", tmp);

  save_binary(tmp, n, ary);
    
  for (i=0; i<n; i++) {
    printf("%d\n", ary[i]);
  }



  return 0;
}
