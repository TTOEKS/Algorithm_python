#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Solved with binary search

typedef struct _CARD_INFO {
  long long number;
  int exist;
} card_info;

int compare(const void *a, const void *b) {
  if (*(long long*)a > *(long long*)b)
    return 1;
  else if (*(long long*)a < *(long long*)b)
    return -1;
  else
    return 0;
}

bool binary_search(long long *arr, int low, int high, long long target) {
  int mid = (int)(high + low) / 2;

  if (high < low) 
    return false;

  if (arr[mid] == target) 
    return true;

  if (arr[mid] < target) {
    return binary_search(arr, mid + 1, high, target);
  } else {
    return binary_search(arr, low, mid - 1, target);
  }
}

void update_card_exist(long long *player_cards, int num_card, card_info *card) {
  if (binary_search(player_cards, 0, num_card - 1, card->number) == true) 
    card->exist = 1;
  else
    card->exist = 0;
}

int main(int argc, char **argv)
{
  int i;
  int num_player_card = 0;
  long long player_cards[500000] = {0, };
  int num_comp_card = 0;
  card_info comp_cards[500000] = {0, };

  scanf("%d", &num_player_card);
  for (i = 0; i < num_player_card; i++) {
    scanf("%lld", &player_cards[i]);
  }

  qsort(player_cards, num_player_card, sizeof(long long), compare);

  scanf("%d", &num_comp_card);
  for (i = 0; i < num_comp_card; i++) {
    scanf("%lld", &comp_cards[i].number);
    update_card_exist(player_cards, num_player_card, &comp_cards[i]);
  }

  for (i = 0; i < num_comp_card; i++) {
    printf("%d ", comp_cards[i].exist);
  }
  printf("\n");

  return 0;
}
