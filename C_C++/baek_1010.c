#include <stdio.h>

int solve(int N, int M) {
  int res = 1;
  for (int i=0; i<N; i++) {
    res *= (M - i);
    res /= (i + 1);
  }

  return res;
}



int main (int argc, char **argv)
{
  int T, N, M;

  scanf("%d", &T);

  for (int i=0; i<T; i++) {
    scanf("%d %d", &N, &M);
    printf("%d\n", solve(N, M));
  }
}

