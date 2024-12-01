#include <iostream>
#include <vector>

using namespace std;

int matrix[100][100];

/*
* 해당 문제는 푸는 방법을 잘못 생각함
*  본인 생각: 겹치는 넓이를 빼는 것
*  -> 겹치는 부분이 3개 이상일 경우 복잡해짐
*
*  중복되는 것은 스킵할 수 있는 방안을 고민했어야 함
*/
int draw_rectangle(pair<int, int> point) {
  int num_convert = 0;

  for (int i=0; i<10; i++) {
    for (int j=0; j<10 ; j++) {
      if (matrix[i + point.first][j + point.second] == false) {
        matrix[i + point.first][j + point.second] = true;
        num_convert++;
      }
    }
  }
  return num_convert;
}

int main(int argc, char **argv)
{

  for (int i=0; i<100; i++) {
    for (int j=0; j<100; j++) {
      matrix[i][j] = false;
    }
  }

  int N, RES = 0;
  int x, y;
  vector<pair<int, int>> points;

  cin >> N;
  for (int i=0; i<N; i++) {
    cin >> x >> y;
    points.push_back({x, y});
  }

  for (const auto &p: points) {
    RES += draw_rectangle(p);
  }

  cout << RES << endl;

  return 0;

}
