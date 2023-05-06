#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solve(int *card_list, int card_num, int max_num) {
  int result = 0;
  int tmp_result = 0;
  int i,j,k = 0;

  // Hmmmmmmmm.....
  for (i=0; i<card_num; i++) {
    for (j=i+1; j<card_num; j++) {
      for (k=j+1; k<card_num; k++) {
        tmp_result = card_list[i] + card_list[j] + card_list[k];
        if (tmp_result <= max_num && tmp_result > result) {
          result = tmp_result;
        }
      }
    }
  }

  return result;
}

int main(int argc, char **argv)
{
  int card_num, max_num;
  int card[128] = {0, };
  int idx = 0;
  int result = 0;

  scanf("%d %d", &card_num, &max_num);

  for (idx=0; idx<card_num; idx++) {
    scanf("%d", &card[idx]);
  }

  result = solve(card, card_num, max_num);
  printf("%d\n", result);

  return 0;
}
