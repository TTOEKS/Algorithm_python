#include <stdio.h>

#define MAX_STUDENTS  1001
#define NUM_GRADES  6

int num_students;
int class_infos[MAX_STUDENTS][NUM_GRADES];

int check_friends(int student) {
  int i, j;
  int res = 0;

  for (i=1; i<=num_students; i++) {
      if (i == student)
        continue;

    for (j=1; j<NUM_GRADES; j++) {
      if (class_infos[student][j] == class_infos[i][j]) {
        res++;
        break;
      }
    }
  }

  return res;
}

int main(int argc, char **argv)
{
  int i, j, tmp = 0, max = -1, res = -1;

  scanf("%d", &num_students);
  for (i=1; i<=num_students; i++) {
    for (j=1; j<NUM_GRADES; j++) {
      scanf("%d", &class_infos[i][j]);
    }
  }

  for (i=1; i<=num_students; i++) {
    tmp = check_friends(i);
    if (max < tmp) {
      res = i;
      max = tmp;
    }
  }

  printf("%d\n", res);
}
