#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

#define DEAD_TILE    -1
#define EMPTY_TILE    0
#define APPLE_TILE    1
#define SNAKE_TILE    2


#define LEFT    0
#define UP      1
#define RIGHT   2
#define DOWN    3

typedef struct _Move {
  int seconds;
  char direction;
} Move;

typedef struct _SnakeLocate {
  int x;
  int y;
} SnakeLocate;

typedef struct _AppleLocate {
  int x;
  int y;
} AppleLocate;


int board[102][102] = {DEAD_TILE};
int board_size = 0;
AppleLocate apple_locate[100];
 
Move move_queue[100];
int move_front;
int move_rear;

SnakeLocate snake_locate[20000];
int snake_front = 0;
int snake_rear = 0;
int snake_dir = RIGHT;
int snake_size = 1;
int snake_x = 1;
int snake_y = 1;

int total_move_count = 0;

void enqueue_move(int move_second, char turn_dir) {
  move_queue[move_rear].seconds = move_second;
  move_queue[move_rear].direction = turn_dir;
  move_rear++;
}

Move *dequeue_move() {
  if ((move_rear - move_front) <= 0) 
    return NULL;

  Move *move = malloc(sizeof(Move));

  move->seconds = move_queue[move_front].seconds;
  move->direction = move_queue[move_front].direction;
  move_front++;

  return move;
}

void enqueue_snake_locate(int x, int y) {
  snake_locate[snake_rear].x = x;
  snake_locate[snake_rear].y = y;
  snake_rear++;
}

SnakeLocate *dequeue_snake_locate() {
  SnakeLocate *locate = malloc(sizeof(SnakeLocate));

  if ((snake_rear - snake_front) <= 0)
    return NULL;

  locate->x = snake_locate[snake_front].x;
  locate->y = snake_locate[snake_front].y;
  snake_front++;


  return locate;
}

void display_board(bool animated) {
  int i, j;

  if (animated) {
    system("clear");
  }
  printf("[%d] ###################\n", total_move_count);
  for (i = 0; i <= board_size + 1; i++) {
    for (j = 0; j <= board_size + 1; j++) {
      if (board[i][j] == DEAD_TILE)
        printf("# ");
      else if (board[i][j] == SNAKE_TILE)
        printf("\x1b[32m@ \x1b[0m");
      else
        printf("%d ", board[i][j]);
    }
    printf("\n");
  }
}

void init_board(int board_size, int num_apple, AppleLocate *locate) {
  int i;

  for (i = 0; i < 102 * 102; i++) { 
    board[i / 102][i % 102] = DEAD_TILE;
  }

  for (i = 0; i < board_size * board_size; i++) {
    board[i / board_size + 1][i % board_size + 1] = EMPTY_TILE;
  }

  for (i = 0; i < num_apple; i++) {
    board[locate[i].x][locate[i].y] = APPLE_TILE;
  }

  board[snake_x][snake_y] = SNAKE_TILE;
  enqueue_snake_locate(snake_x, snake_y);
}

void init_queue() {
  snake_front = 0;
  snake_rear = 0;
  move_front = 0;
  move_rear = 0;
}

bool move_snake() {
  int target_tile;
  SnakeLocate *locate;
  // usleep(8000);
  // display_board(true);

  total_move_count++;
  switch(snake_dir) {
    case RIGHT:
      snake_y++;
      break;
    case LEFT:
      snake_y--;
      break;
    case UP:
      snake_x--;
      break;
    case DOWN:
      snake_x++;
      break;
  }

  target_tile = board[snake_x][snake_y];

  switch(target_tile) {
    case DEAD_TILE:
    case SNAKE_TILE:
      return false;
      break;
    case APPLE_TILE:
      snake_size++;
      break;
    default:
      board[snake_x][snake_y] = SNAKE_TILE;
      break;
  }

  board[snake_x][snake_y] = SNAKE_TILE;
  enqueue_snake_locate(snake_x, snake_y);

  while ((snake_rear - snake_front) > snake_size) {
    locate = dequeue_snake_locate();
    board[locate->x][locate->y] = EMPTY_TILE;
    free(locate);
  }

  return true;
}

void update_direction(char direction) {
  switch(direction) {
    case 'L':
      if (snake_dir == 0)
        snake_dir = DOWN;
      else 
        snake_dir = (snake_dir - 1) % 4;
      break;
    case 'D':
      snake_dir = (snake_dir + 1) % 4;
      break;
  }
}

void process(int num_queue) {
  int i, j, move_seconds;
  Move *move;

  for (i = 0; i < num_queue; i++) {
    move = dequeue_move();
    move_seconds = move->seconds - total_move_count;
    for (j = 0; j < move_seconds; j++) {
      if (!move_snake()) {
        return ;
      }
    }
    update_direction(move->direction);
    free(move);
  }
  while (move_snake());

  return ;
}


int main(int argc, char **argv)
{
  int i, x, y;
  int num_apple;
  int move_count, num_move;
  char turn_dir;
  
  scanf("%d", &board_size);
  scanf("%d", &num_apple);
  for (i = 0; i < num_apple; i++) {
    scanf("%d %d", &x, &y);
    apple_locate[i].x = x;
    apple_locate[i].y = y;
  }
  scanf("%d", &move_count);
  for (i = 0; i < move_count; i++) {
    scanf("%d %c", &num_move, &turn_dir);
    enqueue_move(num_move, turn_dir);
  }

  init_board(board_size, num_apple, apple_locate);
  // display_board(false);
  process(move_count);
  printf("%d\n", total_move_count);

  return 0;
}
