#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define P_OPEN    '('
#define P_CLOSE   ')'

/*
   1. 변수 초기화 신경 쓸 것
   2. 반복문에 자원 많이 소모되는 함수 사용은 자제할 것
 */

bool stack[50001] = {false, };
int top;
int num_pipe = 0;

void init_stack() {
  top = -1;
}

void push_stack() {
  top++;
  stack[top] = true;
}

void pop_stack() {
  stack[top] = false;
  top--;
}

int count_stack() {
  return top + 1;
}


int main(int argc, char **argv)
{
  int i, l, rc = 0;
  char pipes[100001];

  scanf("%s", pipes);
  init_stack();

  l = strlen(pipes)
  for(i=0 ;i<l; i++) {
    if (pipes[i] == P_CLOSE) {
      pop_stack();
      if (pipes[i - 1] == P_OPEN)
        rc += count_stack();
      else {
        rc++;
      }
    }
    if (pipes[i] == P_OPEN) {
      push_stack();
    }
  }
  printf("%d\n", rc);

  return 0;
}
