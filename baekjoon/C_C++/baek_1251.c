#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
  * 브루드포스 판단 근거
  *   1. 넉넉한 실행 시간
  *   2. 작은 데이터 셋
  *   3. 데이터 셋에 비해 널널한 메모리
  */

int comp(const void *a, const void *b) {
  return strcmp((char *)a, (char *)b);
}

void save_str(char src[], int num1, int num2, int str_len, char dst[]) {
  int cnt = 0;

  if (num1 > num2)
    return ;

  for (int i=num1; i>-1; i--) {
    dst[cnt++] = src[i];
  }

  for (int i=num2; i>num1; i--) {
    dst[cnt++] = src[i];
  }

  for (int i=str_len-1; i>num2; i--) {
    dst[cnt++] = src[i];
  }
}


int main(int argc, char **argv) 
{
  char str[51];
  char str_ary[1500][51];
  int str_len, i, j, cnt = 0;

  memset(str_ary, 0x00, sizeof(str_ary));
  scanf("%s", str);
  str_len = strlen(str);

  for (i=0; i<str_len-2; i++) {
    for (j=1; j<str_len-1; j++) {
      if (i < j)
        save_str(str, i, j, str_len, str_ary[cnt++]);
    }
  }

  qsort(str_ary, cnt, sizeof(str_ary[0]), comp);
  printf("%s\n", str_ary[0]);

  return 0;
}

