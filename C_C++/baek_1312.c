#include <stdio.h>
#include <math.h>

int main()
{
  int A, B, N;
  int tmp;

  scanf("%d %d %d", &A, &B, &N);

  tmp = A;
  for (int i=0; i<N; i++) {
    tmp = (tmp % B) * 10;
  }
  printf("%d\n", tmp/B);
  

  return 0;
}
