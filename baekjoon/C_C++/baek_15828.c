#include <stdio.h>

int packets[200000];
int front;
int rear;
int buffer_num = 0;

int queue_length() {
  return rear - front;
}

void enqueue_packet(int packet) {
  if (queue_length() >= buffer_num)
    return ;

  packets[rear++] = packet;
}

int dequeue_packet() {
  int rc = 0;
  if (queue_length() <= 0) 
    return -1;

  rc = packets[front++];

  return rc;
}

int main(int argc, char **argv)
{
  int packet = 0, tmp = 0;
  int i = 0;

  scanf("%d", &buffer_num);
  do {
    scanf("%d", &packet);
    if (packet == -1)
      break;
    else if (packet == 0)
      dequeue_packet();
    else
      enqueue_packet(packet);
  } while (packet != -1);

  tmp = queue_length();

  if (tmp == 0) {
    printf("empty");
  } else {
    for (i=0; i<tmp; i++) {
      printf("%d ", dequeue_packet());
    }
  }
  printf("\n");

  return 0;

}
