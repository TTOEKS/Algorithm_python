#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct _Node {
  int data;
  struct _Node *next;
} Node;

typedef struct _Queue {
  Node *front;
  Node *rear;
  int count;
} Queue;

void initQueue(Queue *queue) {
  queue->front = NULL;
  queue->rear = NULL;
  queue->count = 0;
}

bool enQueue(Queue *queue, int value) {
  Node *node = malloc(sizeof(Node));

  if (queue == NULL) {
    printf("queue is not initialize\n");
    return false;
  }

  node->data = value;
  node->next = NULL;

  if (queue->count == 0) {
    queue->front = node;
  } else {
    queue->rear->next = node;
  }
  queue->rear = node;

  queue->count++;
  return true;
}

int deQueue(Queue *queue) {
  int rc = 0;
  Node *tmp;

  if (queue == NULL) {
    printf("queue is not initialize\n");
    return false;
  }
  rc = queue->front->data;

  tmp = queue->front;
  queue->front = queue->front->next;

  queue->count--;
  free(tmp);
  return rc;
}
 
int main(int argc, char **argv)
{
  int i, val;
  int num = 0;
  Queue queue;

  scanf("%d", &num);

  initQueue(&queue);
  for (i = 1; i <= num; i++) {
    enQueue(&queue, i);
  }

  while (queue.count != 1) {
    deQueue(&queue);
    if (queue.count == 1)
      break;

    val = deQueue(&queue);
    enQueue(&queue, val);
  }

  printf("%d\n", deQueue(&queue));

  return 0;
}
