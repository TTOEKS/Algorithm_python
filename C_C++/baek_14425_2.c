#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Solved with Linked-list hashing

#define NUM_BUCKET  10000

typedef struct _Node *NodePointer;
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

void chainging(NodePointer node) {
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
  while(cur != NULL) {
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

int main(int argc, char **argv)
{
  int i, count = 0;;
  int numN, numM;
  char buffer[501] = {0, };

  scanf("%d %d", &numN, &numM);

  for (i = 0; i < numN; i++) {
    NodePointer node = malloc(sizeof(Node));
    scanf("%s", buffer);
    initNode(node, buffer);
    }

  for (i = 0; i< numM; i++) {
    scanf("%s", buffer);
    if (searching(buffer) == 1) {
      count++;
    }
  }

  printf("%d\n", count);

  return 0;
}




