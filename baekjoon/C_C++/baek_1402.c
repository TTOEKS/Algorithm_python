#include <stdio.h>

/*
 * 모든 경우 가능
 * A = 5 인경우
 *   * 5보다 큰 경우 모두 가능
 *   -> 5 = 5 * 1 * 1 ...
 *  * 5 보다 작은 경우 모두 가능
 *   -> 5 = 5 * 1 * -1 * -1 * -1 * -1 * 1
 *  * 5 인 경우
 *   -> 5 = 5 * 1 * 1 * -1 * -1
  */

int main()
{
  int i, N;
  long long A, B;

  scanf("%d", &N);
  for (i=0; i<N; i++) {
    scanf("%lld %lld", &A, &B);
    printf("yes\n");
  }

  return 0;
}
