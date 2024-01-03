#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int sum_each_digit(int n, int digit) {
  int idx = 0;
  int sum = 0;

  for (idx = digit ; idx >= 0; idx--) {
    sum += (int)(n / pow(10, idx));
    n = n % (int)pow(10, idx);
  }

  return sum;
}

int get_digit(int n) {
  int digit=1;

  for (digit=1; digit<=6; digit++) {
    if (n < pow(10, digit))
      return digit;
  }

  return 0;
}

int solution(int n) {
  int idx = get_digit(n);
  int tmp_result = 0;

  for (; idx <= n; idx++) {
    tmp_result = sum_each_digit(idx, get_digit(idx));
    tmp_result += idx;

    if (tmp_result == n) {
      return idx;
    }
  }

  return 0;
}

int main(int argc, char **argv)
{
  int n = 0;
  int rc = 0;
  
  scanf("%d", &n);

  printf("%d\n", solution(n));

  return 0;
}
