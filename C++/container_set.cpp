#include <set>
#include <iostream>

// 셋 (set)
/* 중복을 허용하지 않고, 저장된 데이터를 자동으로 정렬하는 컨테이너 (집합)
*/

using namespace std;

int main(int argc, char **argv)
{
  // set initialize
  set<int> s1;
  set<int> s2 = {3, 1, 2, 5, 6};
  set<int> s3(s2);

  set<int> numbers = {1, 2, 3, 4, 5};
  int targets[] = {3, 7};

  for (int target: targets) {
    // 복잡도: O(log N)
    auto it = numbers.find(target);

    if (it != numbers.end()) {
      cout << "원소: " << target << "를 찾았습니다. 값: " << *it << endl;
    } else {
      cout << "원소: " << target << "를 찾지 못했습니다." << endl;
    }
  }

  // 복잡도: O(log N) -> 정렬 필요
  s2.insert(4);
  s2.erase(2);

  auto it = s2.find(4);
  if (it != s2.end()) {
    s2.erase(it);
  }

  return 0;


}
