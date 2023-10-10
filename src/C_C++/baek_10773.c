#include <stdio.h>
#include <stdlib.h>

typedef struct _stack {
  int data[100000];
  int top;
}stack;

void init_stack(stack *Stack) {
  Stack->top = -1;
}

void push_stack(stack *Stack, int value) {
  if (Stack->top >= 100000) {
    printf("No space in stack\n");
    return;
  }

  Stack->data[Stack->top + 1] = value;
  Stack->top++;
}

int pop_stack(stack *Stack) {
  int rc = 0;

  if (Stack->top < 0) {
    printf("No data in stack\n");
    return -1;
  }

  rc = Stack->data[Stack->top];

  Stack->data[Stack->top] = 0;
  Stack->top--;

  return rc;
}


int main(int argc, char **argv)
{
  int i, tmp;
  int num = 0, sum = 0;
  stack Stack;
  init_stack(&Stack);

  scanf("%d", &num);
  for (i = 0; i < num; i++) {
    scanf("%d", &tmp);
    if (tmp != 0)
      push_stack(&Stack, tmp);
    else
      pop_stack(&Stack);
  }

  tmp = Stack.top;
  for (i = 0; i <= tmp; i++) {
    sum += pop_stack(&Stack);
  }

  printf("%d\n", sum);

  return 0;
}
