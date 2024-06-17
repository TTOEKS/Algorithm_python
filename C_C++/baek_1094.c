#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INIT_LENGTH 64

typedef struct _StackType {
  int top;
  int count;
  int node[16];
} StackType;

void init_stack(StackType *s) {
  s->top = -1;
  s->count = 0;
  memset(s->node, 0x00, sizeof(s->node));
}

void push(StackType *s, int data) {
  s->node[++s->top] = data;
  s->count++;
}

int pop(StackType *s) {
  if (s->count <= 0) {
    fprintf(stderr, "NO data in stack\n");
    return -1;
  }

  s->count--;
  return s->node[s->top--];
}

int sum_stack(StackType *s) {
  int sum = 0;
  for (int i=0; i<s->count; i++) {
    sum += s->node[i];
  }
  return sum;
}


int solve(int hope) {
  int sum = 0;
  StackType *stack = malloc(sizeof(StackType));
  init_stack(stack);

  push(stack, INIT_LENGTH);
  sum = sum_stack(stack);

  while (sum != hope) {
    if (sum == hope)
      break;

    int tmp = pop(stack) / 2;
    
    push(stack, tmp);
    sum = sum_stack(stack);

    if (sum < hope) {
      push(stack, tmp);
    }
  }

  return stack->count;
}

int main(int argc, char **argv) 
{
  int X;

  scanf("%d", &X);
  printf("%d\n", solve(X));

}
