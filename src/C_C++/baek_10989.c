#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void display_count(int *count) {
  int i, j;
  
  for (i = 0; i < 10000; i++) {
    for (j = 0; j < count[i]; j++) {
      printf("%d\n", i + 1);
    }
  }
}

int main (int argc, char **argv)
{
  int i = 0;
  int input_num = 0;
  int input = 0;
  int count[10000] = {0, };

  scanf("%d", &input_num);

  for (i = 0; i < input_num; i++) {
    scanf("%d", &input);
    count[input - 1] = count[input - 1] + 1;
  }

  display_count(count);

  return 0;
}
