// 반복자
/* 반복자는 C++에서 컨테이너 (Vector, Set, Map, ...)의 종류와 관계 없이 원소들을
 * 순회하고 접근할 수 있도록 해준다.
 *   - 일관된 방식으로 다양한 컨테이너를 다룰 수 있도록 해줌
 *   - 모든 컨테이너를 같은 방식으로 순회하기 때문에, 컨테이너 수정에도 코드
 * 변경 필요 없음
 *   - 즉, 유지보수와 재사용성이 크게 상승
 * 다양한 반복자 중, 대표적으로 '순방향 반복자', '역방향 반복자'가 있음
 *
 * Vector의 내부구조는 배열, Map은 이진 탐색 트리로 구성되어 있다.
 *   - 각 구성에 맞는 코드를 작성할 필요가 있음
 */

#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

// 순방향 반복자 (Forward interator)
/*
 * 컨테이너의 원소를 순차적으로 순회할 수 있도록 해준다.
 *   - begin(), end()가 쌍으로 나오는 경우가 많음
 *   - begin(): 컨테이너의 첫 원소 위치 / end(): 컨테이너의 마지막 원소 위치
 *   - begin()부토 end() 까지 순회해라
 *   - 특정 원소를 탐색하거나, 조건에 맞는 원소를 찾아 위치를 반환하거나 end()를
 * 반환
 */

void forward_iterator() {
  vector<int> vec = {10, 20, 30, 40, 50};

  for (auto it = vec.begin(); it != vec.end(); ++it) {
    cout << *it << " ";
  }
  cout << endl;

  auto result = find(vec.begin(), vec.end(), 30);
  if (result != vec.end()) {
    cout << "Found: " << *result << endl;
  } else {
    cout << "Not found " << endl;
  }

  map<string, int> myMap = {{"apple", 1}, {"banana", 2}, {"cherry", 3}};

  for (auto it = myMap.begin(); it != myMap.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
  }

  // 역방향 반복자
  /*
   * 컨테이너의 끝에서 시작으로 이동하며 순회한다.
   *  - rbegin()와 rend() 함수를 사용
   *  - rbegin(): 맨 마지막 원소의 위치
   *  - rend(): 맨 처음 원소의 바로 직전 위치
   */

  for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
    cout << *it << " ";
  }
  cout << endl;

  auto res = find(vec.rbegin(), vec.rend(), 30);
  if (res != vec.rend()) {
    cout << "Found: " << *res << endl;
  } else {
    cout << "Not found" << endl;
  }

  return;
}
