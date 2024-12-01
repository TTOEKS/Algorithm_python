#include <vector>

using namespace std;

// 벡터 (Vector)
/*
 * 배열과 매우 유사한 컨테이너로, 데이터를 순차적으로 저장하고 인덱스를 통해 특정 위치에 접근한다.
 * 실제로 배열 대신 백터를 사용해서 문제를 푸는 상황이 더 많음
 * 백터의 내부는 배열로 구성되어 있기 때문에, 맨 뒤에서의 삽입, 삭제 연산은 효율적임
 * 그러나, 맨 앞에서 원소를 삽입, 삭제하는 연산에서는 매우 비효율적 (원소들이 한칸씩 이동해야 함)
 * 맨 앞 원소를 효율적으로 삽입, 삭제하기 위해서는 덱(Deque) 자료구조를 사용해야 함
 */

int main(int argc, char **argv) {
  // Vector initailize
  vector<int> v1;
  vector<int> v2 = {1, 2, 3, 4, 5};
  vector<int> v3(4, 3);
  vector<int> v4(v3);

  v2[2] = 10;

  // 원소 뒤에 삽입/삭제
  v2.push_back(6);
  v2.pop_back();

  // 원소 앞에 삽입/삭제
  v2.insert(v2.begin(), 1);
  v2.erase(v2.begin());

  // 2차원 배열
  vector<vector<int>> v5;

  int rows = 3;
  int cols = 4;
  int val = 9;

  // 2차원 배열 초기화
  vector<vector<int>> v6(rows, vector<int>(cols));
  vector<vector<int>> v7(rows, vector<int>(cols, val));
  vector<vector<int>> v8 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

}
