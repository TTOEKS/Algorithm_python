#include <stdio.h>
#include <string.h>

#define MAX_NUM_WORD  25

char word_stack[5][26] = {'\0', };
int top = 0;

void init_stack() {
  top = -1;
}

void push(char *str) {
  snprintf(word_stack[++top], MAX_NUM_WORD, "%s", str);
}

char *pop() {
  return word_stack[top--];
}

int count_stack() {
  return top;
}


int main(int argc, char **argv)
{
  int top = 0;
  int N = 0, i = 0, j = 0;
  char words[26];
  char *tmp = NULL;

  scanf("%d", &N);
  getchar();

  for (i=0; i<N; i++) {
    tmp = NULL;
    init_stack();
    scanf("%[^\n]", words);
    getchar();

    tmp = strtok(words, " ");
    while (tmp != NULL){
      push(tmp);
      tmp = strtok(NULL, " ");
    }

    printf("Case #%d: ", i+1);
    j = count_stack();
    for (; j>=0; j--) {
      printf("%s ", pop());
    }
    printf("\n");
  }
  return 0;
}
