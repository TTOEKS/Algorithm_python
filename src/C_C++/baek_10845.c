#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STR_PUSH  "push"
#define STR_POP   "pop"
#define STR_SIZE  "size"
#define STR_EMPTY "empty"
#define STR_FRONT "front"
#define STR_BACK  "back"

#define INT_UNKNOWN   -1
#define INT_PUSH      1
#define INT_POP       2
#define INT_SIZE      3
#define INT_EMPTY     4
#define INT_FRONT     5
#define INT_BACK      6


/*
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수 출력 없는 경우 -1
size: 큐에 들어가 있는 정수의 개수를 출력
empty: 큐가 비어있으면 1, 아니면 0
front: 큐의 가장 앞에 있는 정수를 출력, 없는 경우 -1
back: 큐의 가장 뒤에 있는 정수를 출력, 없는 경우 -1
 */

typedef struct _Command {
  int int_cmd;
  int int_arg;
}command;

typedef struct _Node {
  int data;
  struct _Node *next;
} Node;

typedef struct _Queue {
  Node *front;
  Node *rear;
  int count;
} Queue;

Queue queue;
void initQueue() {
  queue.front = NULL;
  queue.rear = NULL;
  queue.count = 0;
}

int is_empty() {
  if (queue.count == 0)
    return 1;
  else
    return 0;
}

int queue_length() {
  return queue.count;
}

void push(int x) {
  Node *node = malloc(sizeof(Node));

  node->data = x;
  node->next = NULL;

  if (is_empty()) {
    queue.front = node;
  } else {
    queue.rear->next = node;
  }
  queue.rear = node;
  queue.count++;
}

int pop() {
  Node *tmp;
  int rc;

  if(is_empty()) 
    return -1;


  rc = queue.front->data;
  
  tmp = queue.front;
  queue.front = queue.front->next;

  free(tmp);
  queue.count--;

  return rc;
}

int queue_front() {
  if (is_empty()) 
    return -1;
  else
    return queue.front->data;
}

int queue_back() {
  if (is_empty())
    return -1;
  else
    return queue.rear->data;
}

void arg_handler(char *str_cmd, command *cmd) {
  int arg = -1;

  if (strcmp(str_cmd, STR_PUSH) == 0) {
    scanf("%d", &arg);
    cmd->int_cmd = INT_PUSH;
  } else if (strcmp(str_cmd, STR_POP) == 0) {
    cmd->int_cmd = INT_POP;
  } else if (strcmp(str_cmd, STR_SIZE) == 0) {
    cmd->int_cmd = INT_SIZE;
  } else if (strcmp(str_cmd, STR_EMPTY) == 0) {
    cmd->int_cmd = INT_EMPTY;
  } else if (strcmp(str_cmd, STR_FRONT) == 0) {
    cmd->int_cmd = INT_FRONT;
  } else if (strcmp(str_cmd, STR_BACK) == 0) {
    cmd->int_cmd = INT_BACK;
  } else {
    cmd->int_cmd = INT_UNKNOWN;
  }
  cmd->int_arg = arg;
}

void do_process(command cmd) {
  switch(cmd.int_cmd) {
    case INT_PUSH:
      push(cmd.int_arg);
      break;
    case INT_POP:
      printf("%d\n", pop());
      break;
    case INT_SIZE:
      printf("%d\n", queue_length());
      break;
    case INT_EMPTY:
      printf("%d\n", is_empty());
      break;
    case INT_FRONT:
      printf("%d\n", queue_front());
      break;
    case INT_BACK:
      printf("%d\n", queue_back());
      break;
    default:
      fprintf(stderr, "Unknwon command\n");
      break;
  }
}

int main(int argc, char **argv)
{
  int i;
  int num_cmd, int_cmd;
  char cmd[8] = {0, };
  command cmds[10000];

  scanf("%d", &num_cmd);

  for (i = 0; i < num_cmd ; i++) {
    scanf("%s", cmd);
    arg_handler(cmd, &cmds[i]);
  }

  for (i = 0; i < num_cmd; i++) {
    do_process(cmds[i]);
  }

  return 0;
}
