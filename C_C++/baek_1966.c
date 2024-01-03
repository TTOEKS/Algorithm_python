#include <stdio.h>
#include <stdlib.h>

typedef struct _PrinterData {
  int idx;
  int pirority;
  struct _PrinterData *next;
} PrinterData;

typedef struct _PrinterQueue {
  PrinterData *front;
  PrinterData *rear;
  int count;
} PrinterQueue;

int static comp(const void *a, const void *b) {
  if (*(int*)a < *(int*)b)
    return 1;
  else if (*(int*)a > *(int*)b)
    return -1;
  else
    return 0;
}

PrinterQueue printer_queue;
int pirority_map[100];

int queue_size() {
  return printer_queue.count;
}

void init_queue() {
  printer_queue.front = NULL;
  printer_queue.rear = NULL;
  printer_queue.count = 0;
}

void enqueue_printer(int idx, int pirority) {
  PrinterData *data = malloc(sizeof(PrinterData));

  data->idx = idx;
  data->pirority = pirority;
  data->next = NULL;

  if (printer_queue.count == 0) {
    printer_queue.front = data;
  } else {
    printer_queue.rear->next = data;
  }
  printer_queue.rear = data;
  printer_queue.count++;

}

PrinterData *dequeue_printer() {
  PrinterData *data;

  if (queue_size() <= 0)
    return NULL;

  data = printer_queue.front;
  printer_queue.front = printer_queue.front->next;
  printer_queue.count--;

  return data;
}

int solve(int M) {
  int cnt = 0;
  PrinterData *data;

  while (1) {
    data = dequeue_printer();
    if (data == NULL)
      break;
    if (data->pirority < pirority_map[cnt]) {
      enqueue_printer(data->idx, data->pirority);
    } else {
      cnt++;
      if (data->idx == M) {
        free(data);
        break;
      }
      free(data);
    }
  }

  return cnt;
}

int main(int argc, char **argv)
{
  int i, j;
  int num_testcase;
  int N, M, tmp;

  PrinterData *data;

  scanf("%d", &num_testcase);
  for (i=0; i<num_testcase; i++) {
    init_queue();
    scanf("%d %d", &N, &M);
    for (j=0; j<N; j++) {
      scanf("%d", &tmp);
      enqueue_printer(j, tmp);
      pirority_map[j] = tmp;
    }
    qsort(pirority_map, N, sizeof(int), comp);
    printf("%d\n", solve(M));
  }
  return 0;
}
