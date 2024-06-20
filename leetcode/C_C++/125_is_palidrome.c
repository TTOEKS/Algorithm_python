#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isPalinderome(char *s) {
  int b_left = 0;
  int b_right = 1;

  int str_len = strlen(s);

  for (int i=0; i<str_len; i++) {
    while (!isalnum(s[i + b_left])) {
      b_left++;
      if (i + b_left == str_len)
        return true;
    }
    
    while (!isalnum(s[str_len - i - b_right])) {
      b_right++;
    }

    if (i + b_left >= str_len - i - b_right)
      break;

    if (tolower(s[i + b_left]) != tolower(s[str_len - i - b_right]))
      return false;
  }
  
  return true;
}

int main(int argc, char **argv)
{
  char input[200002] = {0, };

  scanf("%s", input);
  printf("%d\n", isPalinderome(input));

}

