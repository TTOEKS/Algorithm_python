#include <stdio.h>
#include <stdlib.h>

typedef struct _Student {
  char name[4];
  int student_no;
  struct _Student *next;
} Student;

typedef struct _StudentQueue {
  Student *front;
  Student *rear;
  int count;
} StudentQueue;

StudentQueue student_queue;

void init_queue() {
  student_queue.front = NULL;
  student_queue.rear = NULL;
  student_queue.count = 0;
}

int queue_size() {
  return student_queue.count;
}


void enqueue_student(char *name,  int no) {
  Student *student = malloc(sizeof(Student));

  
  snprintf(student->name, 4, "%s", name);
  student->student_no = no;
  student->next = NULL;

  if (queue_size() == 0) {
    student_queue.front = student;
  } else {
    student_queue.rear->next = student;
  }
  student_queue.rear = student;
  student_queue.count++;
}

Student dequeue_student() {
  Student *tmp;
  Student student;

  snprintf(student.name, 4, "%s", student_queue.front->name);
  student.student_no = student_queue.front->student_no;

  tmp = student_queue.front;
  student_queue.front = student_queue.front->next;
  student_queue.count--;

  free(tmp);

  return student;
}

void find_partner(int student_no) {
  int i;
  Student student_tmp;
  char name[4];

  for (i=0; i<student_no - 1; i++) {
    student_tmp = dequeue_student();
    enqueue_student(student_tmp.name, student_tmp.student_no);
  }
  student_tmp = dequeue_student();
}

int main(int argc, char **argv)
{
  int i;
  int N, student_no;
  char name[4];
  char partner_name[4];

  Student student_tmp;

  init_queue();

  scanf("%d", &N);
  for (i=0; i<N; i++) {
    scanf("%s %d", name, &student_no);
    enqueue_student(name, student_no);
  }

  while (queue_size() > 1) {
    student_tmp = dequeue_student();
    find_partner(student_tmp.student_no);
  }

  student_tmp = dequeue_student();
  printf("%s\n", student_tmp.name);

  return 0;
}




