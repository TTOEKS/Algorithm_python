#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_BUCKET    100000

typedef struct _Node *NodePointer;
typedef struct _Node {
  long long data;
  int cnt;
  NodePointer link;
} Node;

NodePointer hash[NUM_BUCKET];

int hashing(int key) {
  if (key < 0)
    key *= -1;

  return key % NUM_BUCKET;
}


void chaining(NodePointer node) {
  int idx = hashing(node->data);

  if (hash[idx] == NULL) {
    hash[idx] = node;
  } else {
    node->link = hash[idx];
    hash[idx] = node;
  }
}

NodePointer searching(int data) {
  int idx = hashing(data);

  NodePointer cur = hash[idx];

  while (cur) {
    if (cur->data == data)
      return cur;
    cur = cur->link;
  }

  return NULL;
}


void initNode(int data) {
  NodePointer node;

  node = searching(data);
  if (node != NULL) {
    node->cnt++;
  } else {
    node = malloc(sizeof(Node));
    node->data = data;
    node->cnt = 1;
    node->link = NULL;
    chaining(node);
  }
}


int main(int argc, char **argv) {
  int num_N, num_M, i;
  long long data = 0;

  scanf("%d", &num_N);
  for (i = 0; i < num_N; i++) {
    scanf("%lld", &data);
    initNode(data); 
  }

  scanf("%d", &num_M);
  for (i = 0; i < num_M; i++) {
    NodePointer node;

    scanf("%lld", &data);
    node = searching(data);
    if (node != NULL)
      printf("%d ", node->cnt);
    else
      printf("0 ");
  }
  printf("\n");

  return 0;
}
