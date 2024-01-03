#include <stdio.h>

int main(int argc, char **argv)
{
  char text[51];
  int i = 0, num_open = 0;
  int rc = 0;

  scanf("%s", text);

  while (text[i] != '\0') {
    if (text[i] == '(')
      num_open++;
    else
      if (num_open > 0)
        num_open--;
      else
        rc++;
    i++;
  }
  rc += num_open;
  printf("%d\n", rc);
}
