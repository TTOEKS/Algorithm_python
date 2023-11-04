#include <stdio.h>

typedef struct _Queue {
  int arr[100000];
  int front;
  int rear;
}Queue;

void initQueue(Queue *queue) {
  queue->front = 0;
  queue->rear = 0;
}

int isEmpty(Queue *queue) {
  return (queue->rear - queue->front == 0);
}

void enQueue(Queue *queue, int data) {
  queue->arr[queue->rear++] = data;
}

int deQueue(Queue *queue) {
  if (!isEmpty(queue))
    return queue->front++;
  else
    return -1;
}

int front(Queue *queue) {
  return queue->arr[front];
}

int size(Queue *queue) {
  return (queue->rear - queue->front);
}

int main(int argc, char**argv)
{
  int rc = 0;
  int n, k;
  int data, i;
  Queue queue;

  scanf("%d %d", &n, &k);
  init(&queue);

  for (i = 1; i <= n; i++) {
    scanf("%d", &data);

    if (!isEmpty(&queue)) {
      if (size(&queue) % 2 != 0)
        data = !data;
      if (1 >= front(&queue))
        dequeue(&queue);
    }

    if (data == 1) {
      rc++;
      if (i > n - k + 1)
        break;
      else
        enQueue(&queue, i + k - 1);
    }
  }

  if (i <= n)
    printf("Insomnia\n");
  else
    printf("%d\n", rc);

  return 0;
}



