#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE   100000
int HashTable[MAXSIZE][2];

int hashFunc(int data) {
  if (data >= 0)
    return data % MAXSIZE;
  else 
    return (data * -1) % MAXSIZE;
}

void insertHash(int data) {
  int hashAddr = hashFunc(data);
  int negative_flag = 0;
  int insert_data = data;
  
  if (data < 0) {
    negative_flag = 1;
    insert_data *= -1;
  }

  while (HashTable[hashAddr][negative_flag] != -1) {
    hashAddr++;
    hashAddr %= MAXSIZE;
  }

  HashTable[hashAddr][negative_flag] = insert_data;
}

int searchHash(int data) {
  int hashAddr = hashFunc(data);
  int negative_flag = 0;
  int find_data = data;

  if (data < 0) {
    negative_flag = 1;
    find_data *= -1;
  }

  while (HashTable[hashAddr][negative_flag] != -1) {
    if (HashTable[hashAddr][negative_flag] == find_data) {
      return 1;
    } else {
      hashAddr++;
      hashAddr %= MAXSIZE;
    }
  }

  return 0;
}


int main(int argc, char **argv)
{
  int i, tmp;
  int num_input;

  memset(HashTable, -1, sizeof(int) * MAXSIZE);

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
