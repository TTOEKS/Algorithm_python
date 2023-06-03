#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void display_array(int *array, int len) {
  int i = 0;

  for (i = 0; i < len; i++) {
    printf("[%d] %d\n", i, array[i]);
  }
  printf("\n");
}

void switch_value(int *elem1, int *elem2) {
  int tmp;

  tmp = *elem1;
  *elem1 = *elem2;
  *elem2 = tmp;
}

void bubble_sort(int *array, int len) {
  int i, j, tmp;

  printf("### Bubble Sort ###\n");
  for (i = len; i > -1; i--) {
    for (j = 0; j < i - 1; j++) {
      if (array[j] > array[j + 1]) {
        switch_value(&array[j], &array[j + 1]);
      }
    }
  }
}

void select_sort(int *array, int len) {
  int i, j, min, min_idx;

  printf("### Select Sort ###\n");
  for (i = 0; i < len; i++) {
    min = array[i];
    min_idx = i;
    for (j = i; j < len; j++) {
      if (array[j] < min) {
        min = array[j];
        min_idx = j;
      }
    }
    switch_value(&array[min_idx], &array[i]);
  }
}


void insert_sort(int *array, int len) {
  int i, j, key;

  printf("### Insert Sort ###\n");
  for (i = 1; i < len; i++) {
    key = array[i];
    for (j = i; j > 0; j--) {
      if (key < array[j - 1]) 
        array[j] = array[j - 1];
      else 
        break;
    }
    array[j] = key;
  }
}


void quick_sort(int *array, int left, int right) {
  int i = left, j = right, pivot;

  if (i > j)
    return;

  if (i == 0) 
    i++;


  pivot = (int)(left + right)/2;
  switch_value(&array[pivot], &array[0]);

  while (i < j) {
    while (array[0] > array[i])  i++;
    while (array[0] < array[j])  j--;

    if (i <= j)
      switch_value(&array[i++], &array[j--]);
  }

  switch_value(&array[0], &array[j]);
  quick_sort (array, left, j - 1);
  quick_sort (array, j + 1, right);
}

void merge_sort(int *array, int left, int right) {
  int i = left, j = right, mid;
  
  if (left >= right)
    return;

  mid = (i + j) / 2;

  merge_sort(array, left, mid);
  merge_sort(array, mid + 1, right); 

  int count = right - left + 1;
  int sub_left_count = count / 2;
  int sub_right_count = count - sub_left_count;

  int sub_left[sub_left_count];
  int sub_right[sub_right_count];


  i = 0; j = 0;
  for (; i < sub_left_count; i++) {
    sub_left[i] = array[left + i + j];
  }


  for (; j < sub_right_count; j++) {
    sub_right[j] = array[left + i + j];
  }

  int k = left;
  i = 0; j = 0;
  while (i < sub_left_count && j < sub_right_count) {
    if (sub_left[i] <= sub_right[j])
      array[k++] = sub_left[i++];
    else
      array[k++] = sub_right[j++];
  }

  for (; i < sub_left_count; i++) 
    array[k++] = sub_left[i];

  for (; j < sub_right_count; j++) 
    array[k++] = sub_right[j];
}

int main(int argc, char **argv)
{
  int test_array[10] = {3, -1, 2, 5, 7, 9, 3, 4, 5, 10};
  printf("Hello World\n");

  display_array(test_array, 10);

  // bubble_sort(test_array, 10);
  // select_sort(test_array, 10);
  // insert_sort(test_array, 10);
  // printf("### Quick Sort ###\n");
  // quick_sort(test_array, 0, 9);
  printf("### Merge Sort ###\n");
  merge_sort(test_array, 0, 9);

  display_array(test_array, 10);

  return 0;
}


