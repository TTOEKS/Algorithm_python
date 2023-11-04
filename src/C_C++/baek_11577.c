#include <stdio.h>



int main(int argc, char **argv)
{
  int i;
  int n, k;
  int lights[100000];
  int maps[100000];
  int cnt = 0;

  // dataset input
  scanf("%d %d", &n, &k);
  for (i = 1; i <= n; i++) {
    scanf("%d", &lights[i]);
    printf("%d ", lights[i]);
  }
  printf("\n");

  // set maps array with uncontinuational data
  for (i = 1; i <= n; i++) {
    maps[i] = lights[i] ^ lights[i + 1];
    printf("%d ", maps[i]);
  }
  printf("\n");

  for (i = 1; i <= n - k + 2; i++) {
    if (maps[i]) {
      maps[i] ^= 1;
      maps[i + k] ^= 1;
      cnt++;
    }
    printf("%d ", maps[i]);
  }
  printf("\n");

  for (i = n - k + 2; i <= n; i++) {
    printf("%d ", maps[i]);
    if (maps[i]) {
      printf("Insomnia / cnt : %d\n", cnt);
      return 0;
    }
  }
  printf("%d\n", cnt);

  return 0;
}
