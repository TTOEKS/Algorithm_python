#include <stdio.h>
#include <stdlib.h>

typedef struct _Space {
  int car_no;
  int price;
} Space;

typedef struct _CarData {
  int no;
  int weight;
} CarData;


Space space[100];
CarData car_queue[2000];
int car_info[2000];
int front = 0;
int rear = 0;
int earn = 0;
int N, M;

int queue_length() {
  return rear - front;
}

void enqueue_car(int no, int weight) {
  car_queue[rear].no = no;
  car_queue[rear].weight = weight;
  rear++;
}

CarData *dequeue_car() {
  CarData *data = malloc(sizeof(CarData));

  data->no = car_queue[front].no;
  data->weight = car_queue[front].weight;
  front++;

  return data;
}

int alloc_space(int N) {
  int i;

  for (i=0; i<N; i++) {
    if (space[i].car_no == -1)
      return i;
  }

  return -1;
}

int find_car(int car_no) {
  int i;
  
  for (i=0; i<N; i++) {
    if (space[i].car_no == car_no)
      return i;
  }
  return -1;
}


void command_handler(int val) {
  int space_no = 0;

  if (val > 0) {
    space_no = alloc_space(N);
    if (space_no == -1) {
      enqueue_car(val, car_info[val - 1]);
    }
    else {
      space[space_no].car_no = val;
    }

  } else {
    space_no = find_car (val * -1);

    earn += space[space_no].price * car_info[(val*-1) - 1];
    space[space_no].car_no = -1;

    if (queue_length() != 0) {
      CarData *data = dequeue_car();
      space[space_no].car_no = data->no;
    }
  }
}


int main(int argc, char **argv)
{
  int i;
  int val;
 
  scanf("%d %d", &N, &M);

  for (i=0; i<N; i++) {
    scanf("%d", &val);
    space[i].car_no = -1;
    space[i].price = val;
  }

  for (i=0; i<M; i++) {
    scanf("%d", &val);
    car_info[i] = val;
  }

  for (i=0; i<M*2; i++) {
    scanf("%d", &val);
    command_handler(val);
  }
  printf("%d\n", earn);

  return 0;
}
