#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
  int x, y;
  Point(int x, int y): x(x), y(y) {}
};

// sort 함수의 비교함수로 false인 경우 원소 위치 변경
// x값이 작은 구조체가 앞으로, x가 같은 경우 y값이 작은 구조체가 앞으로
bool compare(const Point &a, Point &b) {
  if (a.x == b.x) {
    return a.y < b.y;
  }
  return a.x < b.x;
}

int main(int argc, char **argv)
{
  vector<int> v = {1, 4, 3, 4, 5, 4, 5};

  // ####### count()
  // O(N)
  int ret = count(v.begin(), v.end(), 5);
  cout << ret << endl; // 3

  // ######## sort()
  // sort(시작 반복자, 끝 반복자 (비교 함수))
  // 범위 내 원소들을 오름차순으로 정렬한다.
  // 비교함수가 있는 경우 비교 함수를 기준으로 범위 내 원소를 정렬한다.
  // O(NlogN)

  // 오름차순 정렬
  sort(v.begin(), v.end());

  // 내림차순 정렬
  sort(v.rbegin(), v.rend());

  vector<Point> points = {{3, 4}, {1, 2}, {3, 1}, {2, 5}};
  sort(points.begin(), points.end(), compare);

  for (const Point &p: points) {
    cout << "(" << p.x << ", " << p.y << ") ";
  }
  cout << endl;


  // ######## next_permutation()
  // 가능한 모든 순열을 생성하는 함수이다.
  // 시작 반복자와 끝 반복자를 받아서 사전순으로 순열을 생성한다.
  // 원소 범위 내에서 순열 생성 가능시 true, 불가능시 false 반환
  // 정렬된 상태에서 사용해야 함

  vector<int> permutation_v = {1, 2, 3};

  do {
    for (int i: permutation_v) {
      cout << i << " ";
    }
    cout << endl;
  } while (next_permutation(v.begin(), v.end()));


  // ######### unique()
  // 컨테이너 내 중복되는 원소들을 뒤로 밀어내고 중복되지 않은 원소들만 ㅁ남겨 새로운 범위의 끝 반복자 반환
  // O(N)

  vector<int> unique_v = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5};
  auto newEnd = unique(unique_v.begin(), unique_v.end());

  for (auto it = unique_v.begin(); it != unique_v.end(); ++it) {
    cout << *it << endl;
  }
  cout << endl;


  cout << unique_v.size() << endl;
  for (auto it = unique_v.begin(); it != unique_v.end(); ++it) {
    cout << *it << endl;
  }
  cout << endl;

  // ######### binary_search()
  // 컨테이너에서 주어진 범위 내 원소에 이진 탐색을 수행한다.
  // 이미 원소들이 정렬되어 있어야 정상적으로 동작
  // 시작 반복자, 끝 반복자, 찾을 값 3가지 인자를 전달 받는다.
  // 원소 찾음: True / 원소 못찾음: False
  // O(log N)
  
  vector<int> bs_v = {1, 2, 3, 4, 5};
  cout << binary_search(v.begin(), v.end(), 3) << endl;
  cout << binary_search(v.begin(), v.end(), 7) << endl;

  // ######## max_element(), min_element()
  // 컨테이너 내에서 최대값, 최소값의 위치를 반환하는 함수이다.
  // 시작 반복자, 끝 반복자 2개의 인수를 전달 받는다.
  // O(N)
  
  vector<int> max_min_v = {1, 3, 5, 7, 2, 6, 4};

  auto maxIt = max_element(max_min_v.begin(), max_min_v.end());
  auto minIt = min_element(max_min_v.begin(), max_min_v.end());

  cout << *maxIt << endl;
  cout << *minIt << endl;

  return 0;
}
