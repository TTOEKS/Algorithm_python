#include <stdio.h>
#include <stdlib.h>

int euclidean(int a, int b) {
  if (b == 0)
    return a;
  else
    return euclidean(b, a%b);

}

int main(int argc, char **argv)
{
  int f_up, f_down;
  int s_up, s_down;
  int sum_up, sum_down;
  int euclidean_num = 0;

  scanf("%d %d %d %d", &f_up, &f_down, &s_up, &s_down);
  sum_up = (f_up * s_down) + (f_down * s_up);
  sum_down = f_down * s_down;

  euclidean_num = euclidean(sum_up, sum_down);

  printf("%d %d\n", sum_up / euclidean_num, sum_down / euclidean_num);

  return 0;
}
