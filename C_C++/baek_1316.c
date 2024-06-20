#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _StackType {
  char stack[101];
  int count;
  int top;
} StackType;

void init_stack(StackType *stack) {
  memset(stack->stack, 0x00, sizeof(stack->stack));
  stack->count = 0;
  stack->top = -1;
}

void push(StackType *stack, char ch) {
  stack->stack[++stack->top] = ch;
  stack->count++;
}

char pop(StackType *stack) {
  char res;

  res = stack->stack[stack->top--];
  stack->count--;

  return res;
}

int is_stack_empty(StackType *stack){
  return stack->count == 0;
}

int check_exist_data(StackType *stack, char ch) {
  int i;

  for (i=stack->top; i>=0; i--) {
    if (stack->stack[i] == ch)
      return 1;
  }
  return 0;
}

int check_word_group(char str[]) {
  char *pos = 0;
  char tmp;
  StackType *stack = malloc(sizeof(StackType));

  init_stack(stack);

  pos = str;
  tmp = *pos;
  push(stack, *pos);
  while (*pos != '\0') {
    if (tmp != *pos) {
      if (check_exist_data(stack, *pos)) {
        return 0;
      } else {
        push(stack, *pos);
      }
      tmp = *pos;
    }
    pos++;
  }

  return 1;
}

int main()
{
  int i, N, cnt = 0;
  char words[101] = {'\0', };

  scanf("%d", &N);

  for (i=0; i<N; i++) {
    memset(words, 0x00, sizeof(words));
    scanf("%s", words);
    if (check_word_group(words))
      cnt++;
  }

  printf("%d\n", cnt);

  return 0;
}
