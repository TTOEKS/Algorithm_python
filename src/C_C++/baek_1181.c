#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int compare(const void *a, const void *b) {
  int a_len = strlen(a);
  int b_len = strlen(b);

  if (a_len > b_len)
    return 1;
  else if (a_len < b_len)
    return -1;
  else {
    return strcmp(a, b);
  }
}

int display(char word_list[][64], int num_words) {
  int i, rc;
  char buf[64] = {0, };

  for (i = 0; i < num_words; i++) {
    if ((strncmp(buf, word_list[i], sizeof(buf))) != 0)  {
      snprintf(buf, sizeof(buf), "%s", word_list[i]);
      printf("%s\n", word_list[i]);
    }
  }

  return 0;

}

int main(int argc, char **argv)
{
  int i;
  int num_word = 0;
  char words[20000][64];

  scanf("%d", &num_word);

  for (i = 0; i < num_word; i++) {
    scanf("%s", words[i]);
  }

  qsort(words, num_word, sizeof(words[0]), compare);
  display(words, num_word);

  return 0;
}
