#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MASK 21

int checkline(char *line, char startchr) {
  int i, rc = 0;
  char expect_chr = startchr;

  for (i = 0; i < 8; i++) {
    if (line[i] != expect_chr) {
      rc++;
    }
    expect_chr ^= MASK;
  }

  return rc;
}

int solution(char board[][64], int width, int height) {
  int i, j, k, tmp1, tmp2, tmp_min, min;
  int can_move_width = width - 8;
  int can_move_height = height - 8;
  char expect_chr;

  min = 0;
  for (i = 0; i <= can_move_height; i++) {
    for (j = 0; j <= can_move_width; j++) {
      tmp1 = 0, tmp2 = 0;
      expect_chr = 'B';
      for (k = 0; k < 8; k++) {
        tmp1 += checkline(&board[k + i][j], expect_chr);
        expect_chr ^= MASK;
      }

      expect_chr = 'W';
      for (k = 0; k < 8; k++) {
        tmp2 += checkline(&board[k + i][j], expect_chr);
        expect_chr ^= MASK;
      }

      if (tmp1 < tmp2)
        tmp_min = tmp1;
      else
        tmp_min = tmp2;

      if (min >= tmp_min || (i == 0 && j == 0 ))
        min = tmp_min;
    }
  }

  return min;
}

int main(int argc, char **argv)
{
  int i, j, width, height, result = 0;
  char board[64][64] = {0, };

  scanf("%d %d", &height, &width);

  for (i=0; i<height; i++) {
    scanf("%s", board[i]);
  }

  result = solution(board, width, height);
  printf("%d\n", result);

  return 0;
}

