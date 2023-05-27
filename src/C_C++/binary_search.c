#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int binary_search(int arr[], int target, int low, int high) {
  if (high < low)
    return -1;

  int mid = (int)(high + low) / 2;
  printf("Array mid: %d\n", arr[mid]);
  if (arr[mid] == target)
    return mid;

  if (arr[mid] < target)
    return binary_search(arr, target, mid + 1, high);
  else
    return binary_search(arr, target, low, mid - 1);
}

int main(int argc, char **argv)
{
  int int_arr[10] = {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8};
  int target = 0;
  int rc = 0;

  printf("This sample code for binary saerch\n");
  printf("Input your number: ");
  scanf("%d", &target);

  printf("Array list\n");
  for (int i = 0; i < 10; i++) {
    printf("%d ", int_arr[i]);
  }
  printf("\n");

  rc = binary_search(int_arr, target, int_arr[0], int_arr[9]);

  if (rc == -1)
    printf("%d Not found...\n", target);
  else
    printf("Find number in idx: %d\n", rc);

  return 0;
}
