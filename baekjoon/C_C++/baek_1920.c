#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 100000

/*
 *
입력값의 범위가 -2^31 ~ 2^31 - 1까지
빼기로 비교를 진행하면 오버플로우로 정렬이 제대로 이루어지지 않음
- 2^31을 제대로 정렬 못함
int cmp(const void *a, const void *b){
  return *(int*)a - *(int*)b;
}
  */
int cmp(const void *a, const void *b){
  return *(int*)a > *(int*)b;
}

int binary_search(int arr[], int key, int front, int rear) {
  int mid = (front + rear) / 2;
  int pivot = arr[mid];
  

  if (front >= rear)
    return 0;

  if (pivot == key)
    return 1;
  else if (pivot > key)
    return binary_search(arr, key, front, mid);
  else
    return binary_search(arr, key, mid+1, rear);
}

int main(int argc, char **argv)
{
  int i, arr_num, num, tmp;
  int arr[MAXSIZE] = {0, };

  scanf("%d", &arr_num);
  for (i=0; i<arr_num; i++) {
    scanf("%d", &arr[i]);
  }

  qsort(arr, arr_num, sizeof(int), cmp);

  scanf("%d", &num);
  for (i=0; i<num; i++) {
    scanf("%d", &tmp);
    printf("%d\n", binary_search(arr, tmp, 0, arr_num));
  }

  return 0;
}

