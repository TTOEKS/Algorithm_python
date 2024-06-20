#include <stdio.h>


int input_context(int cnt, char *dst, int bufsize) {

  if (cnt % 2 != 0)
    return -1;

  while (cnt > 0) {
    if (cnt >= 4) {
      snprintf(dst, bufsize, "%s%s", dst, "AAAA");
      cnt -= 4;
    } else if (cnt == 2) {
      snprintf(dst, bufsize, "%s%s", dst, "BB");
      cnt -= 2;
    } else {
      return -1;
    }
  }

  return 0;
}

void solve(char board[]) {
  char res[51] = {0, };
  char *pos = board;
  int cnt = 0;

  while (*pos != '\0') {
    if (*pos == 'X')
      cnt++;
    else if (*pos == '.') {
      if (input_context(cnt, res, 51) == -1) {
        printf("-1\n");
        return;
      }
      snprintf(&res[0], sizeof(res), "%s.", res);
      cnt = 0;
    }
    pos++;
  }

  if (input_context(cnt, res, 51) == -1) {
    printf("-1\n");
    return;
  }

  printf("%s\n", res);
}

int main(int argc, char **argv)
{
  char board[51] = {0, };

  scanf("%s", board);
  solve(board);

  return 0;
}
