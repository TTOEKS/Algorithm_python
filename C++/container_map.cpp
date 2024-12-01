#include <map>
#include <iostream>

// 맵 (Map)
/*
 * 키와 값을 쌍으로 갖는 컨테이너이다.
 *   - 내부는 균형 이진 탐색 트리로 구성되어 있어 항상 키 값을 기준으로 데이터가 자동 정렬되어 있음
 *   - N개의 키가 있는 경우 검색, 삽입, 삭제를 O(log N)에 가능
 *   - 맵은 키 값이 중복되지 않고 유일하다는 특징이 존재함
  */

using namespace std;

int main() 
{
  map<string, double> employeeSalaries;
  map<string, double> studentGrades = {
  {"john", 3.7},
  {"Emma", 3.9},
  {"Sophia", 4.0}
  };
  
  // 주의할 점: 키 값이 없는 경우 아래와 같이 접근 시, 새로운 키를 추가한다
  studentGrades["john"];
  // 새로운 키 추가를 방지하기 위해서는 아래와 같이 사용
  studentGrades.find("Charlie");
  
  studentGrades["Alice"] = 5.0;

  int grade = studentGrades["Alice"];
  cout << grade << endl;

  int grade2 = studentGrades["rabbit"];
  cout << grade2 << endl;

  // 맵은 pair 객체 원소를 가지고 있기 때문에 멤버 변수로 first, second를 가지고 있음
  // first: 맵의 키 정보 / second: 맵의 값 정보
  auto it = studentGrades.find("Charlie");
  if (it != studentGrades.end()) {
    int grade3 = it->second;
    cout << grade3 << endl;
  }

  // 수정
  studentGrades["john"] = 2.3;

  // 추가
  studentGrades.insert(make_pair("Eve", 5.0));
  studentGrades.insert({"Bob", 1.0});

  for (const auto &pair: studentGrades) {
    cout << pair.first << ": " << pair.second << endl;
  }

  // 삭제
  studentGrades.erase("Eve");
  for (const auto &pair: studentGrades) {
    cout << pair.first << ": " << pair.second << endl;
  }

  auto it2 = studentGrades.find("john");
  if (it2 != studentGrades.end()) {
    studentGrades.erase("john");
  }

  for (const auto &pair: studentGrades) {
    cout << pair.first << ": " << pair.second << endl;
  }

  return 0;
}
