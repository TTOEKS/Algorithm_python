#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct _Node {

}

void save_binary(int input, int n, int *save) {
  int i, tmp;
  int value, rest;

  value = input;
  for (i=n - 1; i>-1; i--) {
    tmp = pow(10, i);
    *save++ = value / tmp;
    value %= tmp;
  }
}

int main(int argc, char **argv)
{
  int i, j, tmp;
  int n;
  int matrix[50][50];

  printf("Hello world\n");
  scanf("%d", &n);

  for (i=0; i<n; i++) {
    scanf("%d", &tmp);
    save_binary(tmp, n, matrix[i]);
  }
  printf("##### MATRIX ######\n");
  for (i=0; i<n; i++) {
    for (j=0; j<n; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }



}
