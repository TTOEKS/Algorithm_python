// Solved by zghdls

#include <stdio.h>
#include <stdlib.h>
#define SIZE 1001
#define INF 2000000000

typedef struct{
    int end;
    int weight;
}element;

typedef struct NodeType{
    element data;
    struct NodeType *link;
}NodeType;

typedef struct{
    int numVertex;
    NodeType *adjList[SIZE];
    int distance[SIZE];
}GraphType;

typedef struct{
    int size;
    element heap[SIZE * 10];
}HeapType;

void insert(HeapType *h, int end, int weight){
    h->size++;
    int insertPos = h->size;
    while(insertPos > 1){
        if(h->heap[insertPos/2].weight > weight){
            h->heap[insertPos] = h->heap[insertPos/2];
            insertPos /= 2;
        }
        else {
            break;
        }
    }
    h->heap[insertPos].end = end;
    h->heap[insertPos].weight = weight;
}

element delete(HeapType *h){
    element remove = h->heap[1];
    element comp = h->heap[h->size];
    h->size--;
    int parent = 1;
    int child = 2;
    while(child <= h->size){
        if(child < h->size){
            if(h->heap[child].weight > h->heap[child + 1].weight){
                child++;
            }
        }
        if(h->heap[child].weight < comp.weight){
            h->heap[parent] = h->heap[child];
            parent = child;
            child *= 2;
        }
        else {
            break;
        }
    }
    h->heap[parent] = comp;
    return remove;
}

void init(GraphType *g, GraphType *r, int num){
    g->numVertex = num;
    for(int i = 1; i <= num; i++){
        g->distance[i] = INF;
        g->adjList[i] = NULL;
        r->adjList[i] = NULL;
        r->distance[i] = INF;
    }
}

NodeType *getNode(int end, int weight){
    NodeType *tmp = (NodeType *)malloc(sizeof(NodeType));
    tmp->data.end = end;
    tmp->data.weight = weight;
    tmp->link = NULL;
    return tmp;
}


void insertEdge(GraphType *g, GraphType *r,  int numEdge){
    int start, end, weight;
    for(int i = 0; i < numEdge; i++){
        scanf("%d%d%d", &start, &end, &weight);
        NodeType *new = getNode(end, weight);
        new->link = g->adjList[start];
        g->adjList[start] = new;
        new = getNode(start, weight);
        new->link = r->adjList[end];
        r->adjList[end] = new;
    }
}

void dijkstra(GraphType *g, HeapType *h, int start){
    h->size = 0;
    insert(h, start, 0);
    g->distance[start] = 0;
    int selected = 0;
    element latest;
    while(h->size > 0){
        latest = delete(h);
        if(g->distance[latest.end] < latest.weight){
            continue;
        }
        NodeType *tmp = g->adjList[latest.end];
        while(tmp != NULL){
            int sum = g->distance[latest.end] + tmp->data.weight;
            if(g->distance[tmp->data.end] > sum){
                g->distance[tmp->data.end] = sum;
                insert(h, tmp->data.end, sum);
            }
            tmp = tmp->link;
        }
    }
}

int getMin(GraphType *g, GraphType *r, HeapType *h, int start){
    int max = 0;
    dijkstra(g, h, start);
    dijkstra(r, h, start);
    for(int i = 1; i <= g->numVertex; i++){
        if(max < g->distance[i] + r->distance[i]){
            max = g->distance[i] + r->distance[i];
        }
    }
    return max;
}

GraphType graph, *g = &graph;

GraphType graph_reverse, *r = &graph_reverse; 

HeapType heap, *h = &heap;

int main(){
    int N, M, X;
    scanf("%d%d%d", &N, &M, &X);
    init(g, r, N);
    insertEdge(g, r, M);
    printf("%d", getMin(g, r, h, X));
}


