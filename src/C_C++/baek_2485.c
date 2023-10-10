#include <stdio.h>
#include <stdlib.h>

int euclidean(int a, int b) {
  if (b == 0)
    return a;
  else
    return euclidean(b, a%b);
}

int getGCD(int a[], int n) {
  int i, j, cnt = 0;
  int gcd = a[0];

  for (i = 1; i < n; i++) {
    gcd = euclidean(gcd, a[i]);
  }

  return gcd;
}

int main(int argc, char **argv)
{
  int i, GCD = 0;
  int num_colon = 0;
  int addition_colon = 0;
  int colons[100000] = {0, };
  int distance[100000] = {0, };

  scanf("%d", &num_colon);
  for (i = 0; i < num_colon; i++) {
    scanf("%d", &colons[i]);
  }
  for (i = 0; i < num_colon - 1; i++) {
    distance[i] = colons[i + 1] - colons[i];
  }
  
  GCD = getGCD (distance, num_colon - 1);

  if (GCD != -1) {
    for (i = 0; i < num_colon - 1; i++) {
      if (distance[i] == GCD)
        continue;
      addition_colon += (distance[i] / GCD  - 1);
    }
  } else {
    for (i = 0; i < num_colon - 1; i++) {
      addition_colon += distance[i] - 1;
    }
  }
  printf("%d\n", addition_colon);

  return 0;
}
