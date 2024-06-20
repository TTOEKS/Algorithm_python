#include <stdio.h>

int check_leap_year(int year) {
  int leap_flag = 0;
  
  if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0))
    leap_flag = 1;

  return leap_flag;
}

int calc_days(int year, int month, int days) {
  int res = 0;

  for (int i=0; i<year; i++) {
    res += 365;
    if (check_leap_year(i))
      res++;
  }

  for (int i=1; i<month; i++) {
    switch (i) {
      case 1:
      case 3:
      case 5:
      case 7:
      case 8:
      case 10:
      case 12:
        res += 31;
        break;
      case 4:
      case 6:
      case 9:
      case 11:
        res += 30;
        break;
      case 2:
        if (check_leap_year(year))  {
          res += 29;
        }
        else {
          res += 28;
        }
        break;
    }
  }

  res += days;

  return res;
}

int main()
{
  int s_year, s_month, s_days;
  int d_year, d_month, d_days;
  int s_res, d_res, res;

  scanf("%d %d %d", &s_year, &s_month, &s_days);
  scanf("%d %d %d", &d_year, &d_month, &d_days);

  s_res = calc_days(s_year, s_month, s_days);
  d_res = calc_days(d_year, d_month, d_days);

  res = d_res - s_res;


  if (res == 365243) 
    printf("gg\n");
  else 
    printf("D-%d\n", res);

  return 0;
}
