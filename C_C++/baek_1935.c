#include <stdio.h>

#define MAX_STACK_VALUE   100

double double_stack[101] = {0, };
int top = -2;
int vals[26] = {0, };

void init_stack() {
  top = -1;
}

void push_stack(double value) {
  if (top >= MAX_STACK_VALUE)  {
    fprintf(stderr, "Stack buffer has no space\n");
    return ;
  }
  double_stack[++top] = value;
}

double pop_stack() {
  if (top <= -1) {
    fprintf(stderr, "Stack buffer has no value\n");
    return -1;
  }
  return double_stack[top--];
}

int get_seq_upper(char value) {
  return (int)value - 65;
}

double plus_from_stack() {
  double a, b;

  a = pop_stack();
  b = pop_stack();

  return b + a;
}

double minus_from_stack() {
  double a, b;

  a = pop_stack();
  b = pop_stack();

  return b - a;
}

double time_from_stack() {
  double a, b;

  a = pop_stack();
  b = pop_stack();

  return b * a;
}

double division_from_stack() {
  double a, b;
  
  a = pop_stack();
  b = pop_stack();

  return b / a;
}

void operator_handler(char *operators) {
  int cnt = 0;
  double tmp = 0;

  while (*operators != '\0') {
    switch (*operators) {
      case '+':
        push_stack(plus_from_stack());
        break;
      case '-':
        push_stack(minus_from_stack());
        break;
      case '*':
        push_stack(time_from_stack());
        break;
      case '/':
        push_stack(division_from_stack());
        break;
      default:
        push_stack(vals[get_seq_upper(*operators)]);
        break;
    }
    operators++;
  }
}

int main(int argc, char **argv)
{
  int i = 0;
  int N = 0;
  char operators[101] = {'\0', };

  init_stack();
  scanf("%d", &N);
  scanf("%s", operators);

  for (;i<N; i++) {
    scanf("%d", &vals[i]);
  }

  init_stack();
  operator_handler(operators);
  printf("%.2lf\n", pop_stack());

  return 0;
}
