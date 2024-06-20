#include <stdio.h>

int main() 
{
  int n;
  char *test = "123456789";
  char dest[20] = {0, };

  printf("STR: %s\n", test);
  printf("INPUT NUM: ");
  scanf("%d", &n);

  snprintf(dest, n, "%s", test);
  printf("RESULT: %s\n", dest);
  printf("SIZEOF DEST: %ld\n", sizeof(dest));
  printf("SIZEOF CHAR: %ld\n", sizeof(char));
  printf("COMPARE SIZE 1: %d\n", sizeof(char)*20 == 20);
  printf("COMPARE SIZE 2: %d\n", sizeof(dest) == 20);

  return 0;
}
