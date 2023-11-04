#include <stdio.h>
#include <string.h>

/*
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/


int queue[4000000];
int front;
int rear;

void init_queue() {
  front = 0;
  rear = 0;
}

int size_queue() {
  return rear - front;
}

int is_empty() {
  return !(rear - front) ? 1 : 0;
}


int back_queue() {
  if (is_empty()) 
    return -1;
  else {
    return queue[rear - 1];
  }
}

int front_queue() {
  if (is_empty())
    return -1;
  else {
    return queue[front];
  }
}

void push_queue(int x) {
  queue[rear++] = x;
}

int pop_queue() {
  int rc = 0;

  if (is_empty())
    return -1;

  rc = queue[front];
  front++;

  return rc;
}

void run_function(char *cmd) {
  int arg = 0;

  if (strcmp(cmd, "push") == 0) {
    scanf("%d", &arg);
    push_queue(arg);
  } else if (strcmp(cmd, "pop") == 0) {
    printf("%d\n", pop_queue());
  } else if (strcmp(cmd, "size") == 0) {
    printf("%d\n", size_queue());
  } else if (strcmp(cmd, "empty") == 0) {
    printf("%d\n", is_empty());
  } else if (strcmp(cmd, "front") == 0) {
    printf("%d\n", front_queue());
  } else if (strcmp(cmd, "back") == 0) {
    printf("%d\n", back_queue());
  } else {
    printf("Invalied Command: %s\n", cmd);
    return ;
  }
}


int main(int argc, char **argv)
{
  int i;
  int num_cmd;
  char command[16] = {0, };
  int arg = 0;

  scanf("%d", &num_cmd);
  init_queue();
  for (i=0; i<num_cmd; i++) {
    scanf("%s", command);
    run_function(command);
  }

  return 0;
}
