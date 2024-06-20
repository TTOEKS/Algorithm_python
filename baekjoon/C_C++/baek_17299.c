#include <stdio.h>
#include <stdlib.h>

int num_map[1000001] = {0, };
int stack[1000000] = {0, };
int top = -1;

void push(int value) {
  stack[++top] = value;
}

int pop() {
  return stack[top--];
}

int peak() {
  return stack[top];
}

int isEmpty() {
  return (top == -1);
}


void calc_NGF(int *arr, int *answer_sheet, int arr_num) {
  int i = 0;

  for (i=0; i<arr_num; i++) {
    while (!isEmpty() && (num_map[arr[peak()]] < num_map[arr[i]])) {
      answer_sheet[pop()] = arr[i];
    }
    push(i);
  }
  
  while (!isEmpty()) {
    answer_sheet[pop()] = -1;
  }
}


int main(int argc, char **argv)
{
  int i;
  int arr_num = 0;
  int arr[1000000] = {0, };
  int res[1000000] = {0, };

  scanf("%d", &arr_num);
  for (i=0; i<arr_num; i++) {
    scanf("%d", &arr[i]);
    num_map[arr[i]]++;
  }
  
  calc_NGF(arr, res, arr_num);

  for (i=0; i<arr_num; i++) {
    printf("%d ", res[i]);
  }
  printf("\n");

  return 0;
}
