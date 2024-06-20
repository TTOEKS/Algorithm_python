#include <stdio.h>
#include <stdlib.h>

typedef struct _Truck {
  int weight;
  int time;
} Truck;

typedef struct _TruckQueue {
  Truck trucks[10000];
  int front;
  int rear;
} TruckQueue;

void init_queue(TruckQueue *queue) {
  queue->front = -1;
  queue->rear = -1;
}

int queue_size(TruckQueue *queue) {
  return queue->rear - queue->front;
}

void enqueue(TruckQueue *queue, int w, int l) {
  queue->trucks[queue->rear].weight = w;
  queue->trucks[queue->rear].time = l;
  printf("[ENQUEUE] rear: %d / weight: %d / time :%d\n", queue->rear,
      queue->trucks[queue->rear].weight,
      queue->trucks[queue->rear].time);
  queue->rear++;
}

Truck *dequeue(TruckQueue *queue) {
  Truck *truck_rc = malloc(sizeof(Truck));

  if (queue_size(queue) <= 0)
    return NULL;

  truck_rc->weight = queue->trucks[queue->front].weight;
  truck_rc->time = queue->trucks[queue->front].time;
  /*
  printf("[DEQUEUE] rear: %d / weight: %d / time :%d\n", queue->front,
      queue->trucks[queue->front].weight,
      queue->trucks[queue->front].time);
      */

  queue->front++;

  return truck_rc;
}

int get_queue_front_time(TruckQueue *queue) {
  if (queue_size(queue) <= 0)
    return -1;
  else
    return (queue->trucks[queue->front].time);

}

int main(int argc, char **argv)
{
  int i, weight, loop_count, sum_weight = 0, load_count = 0;
  int N, W, L;
  
  TruckQueue truck_queue;
  Truck *tmp_truck;

  init_queue(&truck_queue);
  scanf("%d %d %d", &N, &W, &L);

  for (i=0; i<N; i++) {
    scanf("%d", &weight);
    sum_weight += weight;

    printf("sum_wieght: %d / queue_size: %d\n", sum_weight,queue_size(&truck_queue));
    printf("\t%d <---> %d\n", get_queue_front_time(&truck_queue), load_count);

    while (sum_weight > L || queue_size(&truck_queue) >= W) {
      tmp_truck = dequeue(&truck_queue);
      sum_weight -= tmp_truck->weight;
      if (tmp_truck == NULL)  break;
      if (queue_size(&truck_queue) > 0 && sum_weight > L) {
        printf("with front data: %d\n", get_queue_front_time(&truck_queue));
        load_count = get_queue_front_time(&truck_queue) + W - 1;
      }
      else  {
        printf("with dequeue data: %d\n",tmp_truck->time);
        load_count = tmp_truck->time + W - 1;
      }
      free(tmp_truck);
    }
    load_count++;
    enqueue(&truck_queue, weight, load_count);
    printf("\n");
  }

  while (queue_size(&truck_queue) > 0) {
    tmp_truck = dequeue(&truck_queue);
    if (tmp_truck == NULL)  break;
    load_count = tmp_truck->time + W;
    free(tmp_truck);
  }
  printf("%d\n", load_count);
}
