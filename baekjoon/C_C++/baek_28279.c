#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
    int data;
    struct _Node *prev;
    struct _Node *next;
} Node;

typedef struct _Deque {
    Node *head;
    Node *tail;
    int size;
} Deque;

void init_deque(Deque *deque) {
    deque->head = NULL;
    deque->tail = NULL;
    deque->size = 0;
}

int size(Deque deque) {
    return deque.size;
}

int empty(Deque deque) {
    return (deque.size == 0);
}

void push_front(Deque *deque, int data) {
    Node *tmp = malloc(sizeof(Node));

    tmp->prev = NULL;
    tmp->data = data;

    if (empty(*deque)) {
        tmp->next = NULL;
        deque->head = tmp;
        deque->tail = tmp;
    } else {
        deque->head->prev = tmp;
        tmp->next = deque->head;
        deque->head = tmp;
    }

    deque->size++;
}

void push_back(Deque *deque, int data) {
    Node *tmp = malloc(sizeof(Node));

    tmp->next = NULL;
    tmp->data = data;

    if (empty(*deque)) {
        tmp->prev = NULL;
        deque->head = tmp;
        deque->tail = tmp;
    } else {
        deque->tail->next = tmp;
        tmp->prev = deque->tail;
        deque->tail = tmp;
    }

    deque->size++;
}

int pop_front(Deque *deque) {
    Node *tmp;

    if (empty(*deque))
        return -1;
    
    tmp = deque->head;
    deque->head = deque->head->next;
    if (deque->head != NULL) 
      deque->head->prev = NULL;

    tmp->next = NULL;
    tmp->prev = NULL;

    deque->size--;
    return tmp->data;
}

int pop_back(Deque *deque) {
    Node *tmp;

    if (empty(*deque))
        return -1;
    
    tmp = deque->tail;
    deque->tail = deque->tail->prev;
    if (deque->tail != NULL) 
      deque->tail->next = NULL;

    tmp->next = NULL;
    tmp->prev = NULL;

    deque->size--;
    return tmp->data;
}

int front(Deque deque) {
    if (empty(deque))
        return -1;
    else
        return deque.head->data;
}

int back(Deque deque) {
    if (empty(deque))
        return -1;
    else
        return deque.tail->data;
}

int deque_handler(Deque *deque, int cmd) {
    int arg;
    int rc = 0;


    switch (cmd) {
        case 1:
            scanf("%d", &arg);
            push_front(deque, arg);
            break;
        case 2:
            scanf("%d", &arg);
            push_back(deque, arg);
            break;
        case 3:
            rc = pop_front(deque);
            printf("%d\n", rc);
            break;
        case 4:
            rc = pop_back(deque);
            printf("%d\n", rc);
            break;
        case 5:
            rc = size(*deque);
            printf("%d\n", rc);
            break;
        case 6:
            rc = empty(*deque);
            printf("%d\n", rc);
            break;
        case 7:
            rc = front(*deque);
            printf("%d\n", rc);
            break;
        case 8:
            rc = back(*deque);
            printf("%d\n", rc);
            break;
        default:
            printf("Unknown command: %d\n", cmd);
            return -1;
            break;
    }

    return rc;
}

int main(int argc, char **argv)
{
    int i;
    int num_command = 0;
    int command = 0;
    Deque deque;

    scanf("%d", &num_command);
    init_deque(&deque);
    for (i=0; i<num_command; i++) {
        scanf("%d", &command);
        deque_handler(&deque, command);
    }

    return 0;
}
