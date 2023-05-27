#include <stdio.h>
#include <stdlib.h>

int comp(const void *comp1, const void *comp2) {
  if (*(int *)comp1 < *(int *)comp2)
    return 1;
  else if (*(int *)comp1 > *(int *)comp2)
    return -1;
  else 
    return 0;
}

int solution(int *user_list, int num_user,  int num_award) {
  int i;

  qsort(user_list, num_user, sizeof(int), comp);

  return user_list[num_award - 1];
}

int main(int argc, char **argv)
{
  int i, num_user, num_award, result;
  int user_list[1024];

  scanf("%d %d", &num_user, &num_award);

  for (i = 0; i < num_user; i++) {
    scanf("%d", &user_list[i]);
  }

  result = solution(user_list, num_user, num_award);
  printf("%d\n", result);

  return 0;

}
