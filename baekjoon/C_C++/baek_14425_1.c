#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Solved with binarySearch

int compare(const void* a, const void* b) { 

  if (strcmp((char *)a, (char *)b) > 0) {
    return 1;
  }
  return 0;
}

bool binary_search(char array[][501], int low, int high, char *target) {
  int mid = (low + high) / 2;
  int rc;

  if (high < low)
    return false;
  
  rc = strcmp(target, array[mid]);

  if (rc == 0)
    return true;

  if (rc > 0)
    return binary_search(array, mid + 1, high, target);
  else
    return binary_search(array, low, mid - 1, target);
}

int main(int argc, char **argv)
{
  int i, rc = 0;
  int num_N, num_M;
  char N[10000][501] = {0, };
  char M[501] = {0, };

  scanf("%d %d", &num_N, &num_M);

  for (i = 0; i < num_N; i++) {
    scanf("%s", N[i]);
  }

  qsort(N, num_N, sizeof(N[0]), compare);
  for (i = 0; i < num_M; i++) {
    scanf("%s", M);
    if (binary_search(N, 0, num_N - 1, M) == true) {
      rc++;
    }
  }

  printf("%d\n", rc);
  return 0;

}
