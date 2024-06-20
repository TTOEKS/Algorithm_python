#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _student {
  int id;
  int cnt;
  int friends[1010];
} student;

typedef struct _stack {
  int array[1010];
  int top;
  int count;
} stack;

int class_infos[1010][6] = {0, };
int num_students = 0;

void init_stack(stack *stack) {
  memset(stack->array, 0x00, sizeof(stack->array));
  stack->count = 0;
  stack->top = -1;
}

void push(stack *stack, int data) {
  stack->array[++stack->top] = data;
  stack->count++;
}


int comp(const void *a, const void *b) {
  const student *student_a = (const student *)a;
  const student *student_b = (const student *)b;

  if (student_a->cnt < student_b->cnt)
    return 1;
  else if (student_a->cnt > student_b->cnt)
    return -1;
  else
    return 0;
}

int check_friends(student s, int id) {
  for (int i=0; i<s.cnt; i++) {
    if (s.friends[i] == id)
      return 1;
  }

  return 0;
}

void count_students(student students[], int grade) {
  int i, j, k, tmp;
  int flag;
  stack *s_student = malloc(sizeof(stack));
  student first_student;


  for (i=1; i<10; i++) {
    init_stack(s_student);
    flag = 0;
    for (j=1; j<=num_students; j++) {
      tmp = class_infos[j][grade];
      if (tmp == i) {
        if (flag) {
          push(s_student, j);
        } else {
          flag = 1;
          first_student = students[j];
        }
      }
    }

    if (flag) {
      push(s_student, first_student.id);
      for (j=0; j<s_student->count; j++) {
        int id = s_student->array[j];
        for (k=0; k<s_student->count; k++) {
          if (id == s_student->array[k])
            continue;
          if (!check_friends(students[id], s_student->array[k])) {
            students[id].friends[students[id].cnt++] = s_student->array[k];
          }
        }
      }
    }
  }
}

int main(int argc, char **argv)
{
  int i, j;
  student students[1010] = {0, };

  scanf("%d", &num_students);
  for (i=1; i<=num_students; i++) {
    for (j=1; j<6; j++) {
      scanf("%d", &class_infos[i][j]);
    }
  }

  for (i=1; i<=num_students; i++) {
    students[i].id = i;
    students[i].cnt = 0;
  }

  for (i=1; i<6; i++) {
    count_students(students, i);
  }

  qsort(&students[1], num_students + 1, sizeof(student), comp);
  printf("%d\n", students[1].id);

  return 0;
}
