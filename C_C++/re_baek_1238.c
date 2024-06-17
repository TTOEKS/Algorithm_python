#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

#define MAX_VERTEX 1001
#define MAX_PATHS  10001

#define INF  INT_MAX
#define TRUE 1
#define FALSE 0

typedef struct _Edge {
  int vertex;
  int weight;
  struct _Edge *link;
} Edge;

typedef struct _GraphType {
  int n;
  Edge *adg_list[MAX_VERTEX];
} GraphType;

typedef struct _node {
  int vertex;
  int distance;
} node;

typedef struct _HeapType {
  int size;
  node  heap[MAX_PATHS];
} HeapType;

int distance[MAX_VERTEX];
int visited[MAX_VERTEX];



HeapType *create_heap() {
  return malloc(sizeof(HeapType));
}

void init_heap(HeapType *heap) {
  heap->size = 0;
}

void insert_heap(HeapType *h, int vertex, int distance) {
  int tmp_idx;
  int insert_idx = ++h->size;
  node new_node;

  new_node.vertex = vertex;
  new_node.distance = distance;

  while (insert_idx != 0 && distance < h->heap[insert_idx/2].distance) {
    h->heap[insert_idx] = h->heap[insert_idx/2];
    insert_idx /= 2;
  }

  h->heap[insert_idx] = new_node;
}

node delete_heap(HeapType *h) {
  node root = h->heap[1];
  node temp = h->heap[h->size--];

  int parent = 1;
  int child = 2;
  
  while (child <= h->size) {
    if ((child < h->size) && h->heap[child].distance < h->heap[child + 1].distance)
      child = child + 1;

    if (temp.distance <= h->heap[child].distance) {
      break;
    }
    
    h->heap[parent] = h->heap[child];
    parent = child;
    child *= 2;
  }

  h->heap[parent] = temp;

  return root;
}

void insert_graph(GraphType *g, int u, int v, int w) {
  Edge *new_edge = malloc(sizeof(Edge));
  new_edge->vertex = v;
  new_edge->weight= w;
  new_edge->link = g->adg_list[u];
  g->adg_list[u] = new_edge;
}

void display_distance(GraphType *g) {
  for (int i=1; i<=g->n; i++) {
    printf("%d ", distance[i]);
  }
  printf("\n");

}

void dijkstra(GraphType *g, int start) {
  HeapType *heap = create_heap();
  init_heap(heap);

  memset(visited, 0x00, sizeof(visited));

  for (int i=0; i<MAX_VERTEX; i++) {
    distance[i] = INF;
  }

  distance[start] = 0;
  insert_heap(heap, start, distance[start]);

  while (heap->size > 0) {
    node cur_node = delete_heap(heap);
    if (!visited[cur_node.vertex]) {
      visited[cur_node.vertex] = TRUE;
      Edge *cur = g->adg_list[cur_node.vertex];

      while (cur) {
        if (distance[cur_node.vertex] + cur->weight < distance[cur->vertex]) {
          distance[cur->vertex] = distance[cur_node.vertex] + cur->weight;
          insert_heap(heap, cur->vertex, cur->weight);
        }
        cur = cur->link;
      }
    }
  }

  // display_distance(g);
  free(heap);
}

int main(int argc, char **argv)
{
  int i, j, tmp, max = -1;
  int n, m, x;
  int start, end, weight;
  int bak_distance[MAX_VERTEX];


  GraphType *g = malloc(sizeof(GraphType));

  scanf("%d %d %d", &n, &m, &x);

  for (i=0; i<m; i++) {
    scanf("%d %d %d", &start, &end, &weight);
    insert_graph(g, start, end, weight);
  }

  g->n = n;
  dijkstra(g, x);

  for (i=1; i<=n; i++) {
    bak_distance[i] = distance[i];
  }
  

  for (i=1; i<=g->n; i++) {
    if (i == x) 
      continue;

    dijkstra(g, i);
    tmp = distance[x] + bak_distance[i];
    if (max < tmp)
      max = tmp;
  }

  printf("%d", max);
  
  return 0;
}

