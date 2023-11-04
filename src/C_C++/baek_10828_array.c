#include <stdio.h>
#include <string.h>

/*
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 출력 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력, 정수가 없는 경우에는 -1을 출력한다.
 */


int stack_array[100000];
int top = 0;

int stack_size() {
  return top;
}

int stack_empty() {
  return (stack_size() <= 0) ? 1 : 0;
}

void stack_push(int x) {
  stack_array[top++] = x;
}

int stack_pop() {
  int rc;

  if (stack_size() <= 0)
    rc = -1;
  else
    rc = stack_array[(top--) - 1];

  return rc;
}

int stack_top() {
  int rc;
  
  if (stack_size() <= 0)
    rc = -1;
  else
    rc = stack_array[top - 1];

  return rc;
}

void command_handler(char *arg) {
  int tmp;

  if (strcmp(arg, "push") == 0) {
    scanf("%d", &tmp);
    stack_push(tmp);
  } else if (strcmp(arg, "pop") == 0) {
    tmp = stack_pop();
    printf("%d\n", tmp);
  } else if (strcmp(arg, "size") == 0) {
    tmp = stack_size();
    printf("%d\n", tmp);
  } else if (strcmp(arg, "empty") == 0) {
    tmp = stack_empty();
    printf("%d\n", tmp);
  } else if (strcmp(arg, "top") == 0) {
    tmp = stack_top();
    printf("%d\n", tmp);
  }
}


int main(int argc, char **argv)
{
  int i;
  int N = 0;
  char command[64];
  
  scanf("%d", &N);

  for (i=0; i<N; i++) {
    scanf("%s", command);
    command_handler(command);
  }
}
