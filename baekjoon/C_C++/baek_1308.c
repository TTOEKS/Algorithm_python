#include <stdio.h>
#include <stdbool.h>

bool is_leap_year(int year) {
  if ((year % 4 == 0 && year % 100 != 0) || (year % 400) == 0)
    return true;

  return false;
}

int calc_day(int year, int mon, int day) {
  int i, res = 0;
  int mon2day[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  for (i=0; i<year; i++) {
    res += 365;
    if (is_leap_year(i))
      res++;
  }

  for (i=1; i<mon; i++) {
    res += mon2day[i];
    if (i == 2 && is_leap_year(year))
      res++;
  }

  res += day;

  return res;
}


int main()
{
  int s_year, s_month, s_day;
  int d_year, d_month, d_day;
  int res = 0;

  scanf("%d %d %d", &s_year, &s_month, &s_day);
  scanf("%d %d %d", &d_year, &d_month, &d_day);

  // if (d_year - s_year >= 1000 && )
  if (d_year - s_year > 1000)
    printf("gg\n");
  else if (d_year - s_year == 1000 && calc_day(0, s_month, s_day) <= calc_day(0, d_month, d_day)){
    printf("gg\n");
  }
  else {
    res = calc_day(d_year, d_month, d_day) - calc_day(s_year, s_month, s_day);

    printf("D-%d\n", res);
  }

  return 0;
}
