#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool stack[30];
int top;

void init_stack() {
  int i = 0;

  for (i=0; i<30; i++) {
    stack[i] = false;
  }
  top = 0;
}

void push_stack() {
  stack[top++] = true;
}

bool pop_stack() {
  if (top <= 0)
    return false;

  stack[top--] = false;
  return true;
}

int count_stack() {
  return top;
}

int solve(char *text) {
  int i, l;

  init_stack();

  l = strlen(text);
  for (i=0; i<l; i++) {
    if (text[i] == '(')
      push_stack();
    else {
      if (!pop_stack()) {
        printf("NO\n");
        return -1;
      }
    }
  }
  if (count_stack() > 0) {
    printf("NO\n");
    return -1;
  } else {
    printf("YES\n");
    return 0;
  }
}


int main(int argc, char **argv)
{
  int i, T;
  char PS[51];

  scanf("%d", &T);
  for (i=0; i<T; i++) {
    scanf("%s", PS);
    solve(PS);
  }

  return 0;
}
