#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
  int data;
  struct _Node *next;
} Node;
typedef struct _Queue {
  Node *front;
  Node *rear;
  int count;
} Queue;

Queue queue;


void initQueue() {
  queue.front = NULL;
  queue.rear = NULL;
  queue.count = 0;
}

void enQueue(int value) {
  Node *node = malloc(sizeof(node));
  
  node->data = value;
  node->next = NULL;

  if (queue.count == 0) {
    queue.front = node;
  } else {
    queue.rear->next = node;
  }
  queue.rear = node;
  queue.count++;
}

int deQueue() {
  int rc = 0;
  Node *tmp;

  rc = queue.front->data;

  tmp = queue.front;
  queue.front = queue.front->next;

  queue.count--;
  free(tmp);

  return rc;
}

void print_josephuse(int n, int k) {
  int i;

  printf("<");
  while (queue.count > 1) {
    for (i = 0; i < k - 1; i++) {
      enQueue(deQueue());
    }
    printf("%d, ", deQueue());
  }
  printf("%d>\n", deQueue());
}

int main(int argc, char **argv)
{
  int i;
  int n, k;

  scanf("%d %d", &n, &k);

  initQueue();
  for (i = 0; i < n; i++) { 
    enQueue(i + 1);
  }
  print_josephuse(n, k);


  return 0;
}


