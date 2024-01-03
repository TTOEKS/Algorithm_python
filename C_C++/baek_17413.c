#include <stdio.h>
#include <string.h>

char str_stack[100003];
int top;

void init_stack() {
  top = -1;
}

void push_stack(char c) {
  str_stack[++top] = c;
}

char pop_stack() {
  return str_stack[top--];
}

int count_stack() {
  return top + 1;
}

void flush_stack() {
  while (count_stack() > 0) {
    printf("%c", pop_stack());
  }
  init_stack();
}

int main(int argc, char **argv)
{
  int i = 0;
  char context[100003];

  fgets(context, 100003, stdin);
  init_stack();
  while (context[i] != '\n') {
    switch(context[i]) {
      case '<':
        flush_stack();
        while (context[i] != '>') printf("%c", context[i++]);
        printf(">");
        break;
      case ' ':
        flush_stack();
        printf(" ");
        break;
      default:
        push_stack(context[i]);
        break;
    }
    i++;
  }
  flush_stack();
  printf("\n");

  return 0;
}
