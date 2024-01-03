#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_BUCKET  1000

typedef struct _Node* NodePointer;
typedef struct _Node {
  char name[21];
  NodePointer link;
} Node;

NodePointer hash[NUM_BUCKET];

int compare(const void *a, const void *b) {
  return strcmp(*(char **)a, *(char **)b);
}

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
  int idx = hashing(stringToint(node->name));

  if (hash[idx] == NULL) {
    hash[idx] = node;
  } else {
    node->link = hash[idx];
    hash[idx] = node;
  }
}

int search(char data[]) {
  int idx = hashing(stringToint(data));

  NodePointer cur = hash[idx];
  while(cur != NULL) {
    if (!strcmp(cur->name, data))
      return 1;
    cur = cur->link;
  }
  return 0;
}

int main(int argc, char **argv)
{
  int i, count = 0;
  int numNL, numNS;
  char NSbuffer[21] = {0, };
  char **NLNS = NULL;

  scanf("%d %d", &numNL, &numNS);
  for (i = 0; i < numNL; i++) {
    NodePointer newNode = malloc(sizeof(Node));
    scanf("%s", newNode->name);
    newNode->link = NULL;
    chainging(newNode);
  }
  
  NLNS = (char**)malloc(sizeof(char*) * numNS);
  for (i = 0; i < numNS; i++) {
    scanf("%s", NSbuffer);
    if (search(NSbuffer)) {
      NLNS[count] = (char *)malloc(sizeof(char) * 21);
      snprintf(NLNS[count], 21, "%s", NSbuffer);
      count++;
    }
  }
  qsort((char**)NLNS, count, sizeof(NLNS[0]), compare);

  printf("%d\n", count);
  for (i = 0; i < count; i++) {
    printf("%s\n", NLNS[i]);
  }

  free(NLNS);
  return 0;
}
