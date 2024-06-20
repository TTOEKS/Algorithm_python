#include <stdio.h>


int queue[2000];
int front;
int rear;


void enqueue(int x) {
  queue[rear++] = x;
}

int dequeue() {
  int rc = 0;
  if (rear - front < 0)
    return -1;

  rc = queue[front];
  front++;

  return rc;
}

void init_queue() {
  int front = 0;
  int rear = 0;
}

int get_queue_size() {
  return rear - front;
}

void solve(int n) {
  while (get_queue_size() >= 1) {
    printf("%d ", dequeue());
    enqueue(dequeue());
  }
}

int main (int argc, char **argv) 
{
  int i;
  int N;

  scanf("%d", &N);

  init_queue();
  for (i=1; i<=N; i++) {
    enqueue(i);
  }

  solve(N);

  return 0;
}
