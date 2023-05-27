#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
  if (*(int *)a > *(int *)b)
    return 1;
  else if (*(int *)a < *(int *)b) 
    return -1;
  else
    return 0;
}

int binary_search(int arr[], int target, int low, int high) {
  if (low > high)
    return -1;

  int mid = (int)(high + low) / 2;

  if (target == arr[mid])
    return mid;

  if (target < arr[mid])
    return binary_search(arr, target, low, mid - 1);
  else
    return binary_search(arr, target, mid + 1, high);

}

int arr_unique(int *arr, int num_arr) {
  int i, num = 1;
  int last_num = arr[0];

  for (i = 0 ;i < num_arr; i++) {
    if (last_num != arr[i]) {
      arr[num++] = arr[i];
      last_num = arr[i];
    }
  }

  memset(arr + num, 0x00, sizeof(int) * (num_arr - num));
  return num;
}

int main(int argc, char **argv)
{
  int i, rc;
  int num_point = 0;
  int atomic_cnt = 0;
  int points[1000000];
  int tmp_buf[1000000];


  scanf("%d", &num_point);

  for (i = 0; i < num_point; i++) {
    scanf("%d", &points[i]);
    tmp_buf[i] = points[i];
  }

  qsort(tmp_buf, num_point, sizeof(int), compare);
  atomic_cnt = arr_unique(tmp_buf, num_point);

  for (i = 0; i < num_point; i++) {
    rc = binary_search(tmp_buf, points[i], 0, atomic_cnt - 1);
    printf("%d ", rc);
  }
  printf("\n");

  return 0;
}


/*
   이진 탐색을 사용할 생각을 하지 못하여, 시간 초과에 발생함
   https://www.acmicpc.net/source/61249657
*/
