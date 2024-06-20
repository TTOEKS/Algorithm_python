#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE   10000

typedef struct _Node {
  int data;
  struct _Node *next;
} Node;

Node *HashTable[214748];

int hashFunc(int data) {
  if (data >= 0)
    return data / MAXSIZE;
  else 
    return (data  / MAXSIZE) * -1;
}

void insertHash(int data) {
  int hashAddr = hashFunc(data);
  Node *node_data = malloc(sizeof(Node));

  node_data->data = data;
  node_data->next = NULL;

  if (HashTable[hashAddr] == NULL)
    HashTable[hashAddr] = node_data;
  else {
    Node *cur = HashTable[hashAddr];
    while (cur->next != NULL) 
      cur = cur->next;
    cur->next = node_data;
  }
}

int searchHash(int data) {
  int hashAddr = hashFunc(data);
  Node *cur;

  cur = HashTable[hashAddr];
  while(cur) {
    if (cur->data == data)
      return 1;
    else {
      cur = cur->next;
    }
  }
  return 0;
}


int main(int argc, char **argv)
{
  int i, tmp;
  int num_input;

  scanf("%d", &num_input);
  for (i=0; i<num_input; i++) {
    scanf("%d", &tmp);
    insertHash(tmp);
  }

  scanf("%d", &num_input);
  for (i=0; i<num_input; i++) {
    scanf("%d", &tmp);
    printf("%d\n", searchHash(tmp));
  }

  return 0;
}
