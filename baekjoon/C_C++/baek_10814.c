#include <stdio.h>
#include <stdlib.h>

typedef struct _Player {
    int join_no;
    int age;
    char name[128];
} player;

int compare(const void *a, const void *b) {
  const player *player1 = a;
  const player *player2 = b;

  if (player1->age > player2->age)
    return 1;
  else if (player1->age == player2->age) {
    if (player1->join_no > player2->join_no) 
      return 1;
    else
      return -1;
  } else {
    return 0;
  }
}

int main(int argc, char **argv)
{
    int i;
    int num_player = 0;
    player *players;

    scanf("%d", &num_player);

    players = (player *)malloc(sizeof(player) * num_player);

    for (i = 0; i < num_player; i++) {
        scanf("%d %s", &players[i].age, players[i].name);
        players[i].join_no = i + 1;
    }

    qsort(players, num_player, sizeof(player), compare);

    for (i = 0; i < num_player; i++) {
        printf("%d %s\n", players[i].age, players[i].name);
    }


    free(players);

    return 0;
}

