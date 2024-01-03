#include <stdio.h>
#include <stdbool.h>

// Solved with hash table

int main (int argc, char **argv)
{
  int i;
  int num_player_card = 0;
  int num_comp_card = 0;
  long long idx = 0;
  bool number_tables[20000001] = {false, };

  scanf("%d", &num_player_card);
  for (i = 0; i < num_player_card; i++) {
    scanf("%lld", &idx);
    number_tables[10000000 + idx] = 1;
  }


  scanf("%d", &num_comp_card);
  for (i = 0; i < num_comp_card; i++) {
    scanf("%lld", &idx);
    if (number_tables[10000000 + idx] == true)
      printf("1 ");
    else
      printf("0 ");
  }
  printf("\n");
  
  return 0;

}
