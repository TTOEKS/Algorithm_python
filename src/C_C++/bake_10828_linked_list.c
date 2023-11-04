#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 출력 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력, 정수가 없는 경우에는 -1을 출력한다.
 */

typedef struct _StackData {
  int data;
  struct _StackData *next;
} StackData;

typedef struct _Stack {
  StackData *top;
  int count;
} Stack;

void init_stack(Stack *stack) {
  stack->top = NULL;
  stack->count = 0;
}

int stack_size(Stack *stack) {
  return stack->count;
}

int stack_empty(Stack *stack) {
  return (stack_size(stack) <= 0) ? 1 : 0;
}

void stack_push(Stack *stack, int x) {
  StackData *data = malloc(sizeof(StackData));

  data->data = x;
  data->next = NULL;

  if (stack_empty(stack)) {
    stack->top = data;
  } else {
    data->next = stack->top;
    stack->top = data;
  }
  stack->count++;
}

int stack_pop(Stack *stack) {
  StackData *tmp;

  if (stack_size(stack) <= 0)
    return -1;
  else
    tmp = stack->top;

  stack->top = stack->top->next;
  stack->count--;
  free(tmp);

  return tmp->data;
}

int stack_top(Stack *stack) {
  return (stack_size(stack) > 0) ? stack->top->data : -1;
}

void command_handler(char *arg, Stack *stack) {
  int tmp;

  if (strcmp(arg, "push") == 0) {
    scanf("%d", &tmp);
    stack_push(stack, tmp);
  } else if (strcmp(arg, "pop") == 0) {
    tmp = stack_pop(stack);
    printf("%d\n", tmp);
  } else if (strcmp(arg, "size") == 0) {
    tmp = stack_size(stack);
    printf("%d\n", tmp);
  } else if (strcmp(arg, "empty") == 0) {
    tmp = stack_empty(stack);
    printf("%d\n", tmp);
  } else if (strcmp(arg, "top") == 0) {
    tmp = stack_top(stack);
    printf("%d\n", tmp);
  }
}


int main(int argc, char **argv)
{
  int i;
  int N = 0;
  char command[64];

  Stack stack;

  init_stack(&stack);
  
  scanf("%d", &N);

  for (i=0; i<N; i++) {
    scanf("%s", command);
    command_handler(command, &stack);
  }

  return 0;
}

