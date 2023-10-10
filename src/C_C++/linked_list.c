#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// LIKED LIST 

#define NUM_BUCKET 100

typedef struct _NodePointer *NodePointer;
typedef struct _Node {
  char data[501];
  NodePointer link;
} Node;

NodePointer hash[NUM_BUCKET];

int stringToint(char *string) {
  int sum = 0;
  while (*string) {
    sum += *string;
    string++;
  }

  return sum;
}

int hashing(int key) {
  return key % NUM_BUCKET;
}

void chaining(NodePointer node) {
  int idx = hashing(stringToint(node->data));

  if (hash[idx] == NULL) {
    hash[idx] = node;
  } else {
    node->link = hash[idx];
    hash[idx] = node;
  }
}

int searching(char data[]) {
  int idx = hashing(stringToint(data));

  NodePointer cur = hash[idx];
  while (cur != NULL) {
    if (!strcmp(cur->data, data))
      return 1;
    cur = cur->link;
  }

  return 0;
}

void initNode(NodePointer node, char *data) {
  snprintf(node->data, 501, "%s", data);
  node->link = NULL;
  chainging(node);
}

