#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Coordinate {
  int x;
  int y;
} coordinate;

void change_coordinate (coordinate *coordi_list, int src, int dst) {
  coordinate tmp_coordinate;

  tmp_coordinate = coordi_list[src];
  coordi_list[src] = coordi_list[dst];
  coordi_list[dst] = tmp_coordinate;
}

int compare_x(const void *a, const void *b) {
  const coordinate *coordi_1  = a;
  const coordinate *coordi_2  = b;

  if (coordi_1->x > coordi_2->x)
    return 1;
  else if (coordi_1->x < coordi_2->x) 
    return -1;
  else
    return 0;
}

int compare_y(const void *a, const void *b) {
  const coordinate *coordi_1  = a;
  const coordinate *coordi_2  = b;

  if (coordi_1->y > coordi_2->y)
    return 1;
  else if (coordi_1->y < coordi_2->y) 
    return -1;
  else
    return 0;
}

int sort_for_y(coordinate *coordi_list, int num_point, int offset) {
  int i, j;

  for (i = num_point; i > 0; i--) {
    for (j = offset; j < offset+ i - 1; j++) {
      if (coordi_list[j].y > coordi_list[j + 1].y) 
        change_coordinate(coordi_list, j, j+1);
    }
  }
  return 0;
}

int solution(coordinate *coordi_list, int num_point) {
  int idx = 0;
  int last_idx = 0;


  qsort (coordi_list, num_point, sizeof(coordinate), compare_x);

  for (idx = 0; idx < num_point - 1; idx++) {
    if (coordi_list[idx].x != coordi_list[idx + 1].x) {
      qsort (&coordi_list[last_idx], (idx - last_idx) + 1, sizeof(coordinate), compare_y);
      last_idx = idx + 1;
    } 
  }

  qsort (&coordi_list[last_idx], (num_point - last_idx), sizeof(coordinate), compare_y);

  return 0;
}


int main(int argc, char **argv)
{
  int num_point = 0;
  int idx = 0;
  coordinate coordi[100000] = {0, };

  scanf("%d", &num_point);
  for (idx = 0; idx < num_point; idx++) {
    scanf("%d %d", &coordi[idx].x, &coordi[idx].y);
  }

  solution(coordi, num_point);
  for (idx = 0; idx < num_point; idx++) {
    printf("%d %d\n", coordi[idx].x, coordi[idx].y);
  }

  return 0;
}

// Better than me: https://www.acmicpc.net/source/60371706
