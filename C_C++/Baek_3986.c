#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
  char data;
  struct _Node *next;
} Node;

typedef struct _Stack {
  Node *top;
  int count;
} Stack;

void init(Stack *stack) {
  stack->top = NULL;
  stack->count = 0;
}

void push(Stack *stack, char character) {
  Node *tmp = malloc(sizeof(Node));

  tmp->data = character;
  tmp->next = stack->top;

  stack->top = tmp;
  stack->count++;
}

char pop(Stack *stack) {
  char rc;
  Node *tmp;

  if (stack->count <= 0)
    return '\0';

  tmp = stack->top;

  rc = tmp->data;
  stack->top = tmp->next;

  free(tmp);
  stack->count--;
  return rc;
}
 
char peek(Stack *stack) {
  char rc;

  if (stack->count <= 0)
    return '\0';

  rc = stack->top->data;
  return rc;
}

int solve(char *text) {
  int i = 0;
  Stack stack;

  init(&stack);

  push(&stack, text[i++]);
  while (text[i] != '\0') {
    if (peek(&stack) == text[i]) {
      pop(&stack);
    } else {
      push(&stack, text[i]);
    }
    i++;
  }

  if (stack.count == 0)
    return 1;
  else
    return 0;
}

int main(int argc, char **argv)
{
  int i, N; 
  int count = 0;
  char text[100001];

  scanf("%d", &N);
  for (i=0; i<N; i++) {
    scanf("%s", text);
    if (solve(text) == 1)
      count++;
  }
  printf("%d\n", count);
  
  return 0;
}
