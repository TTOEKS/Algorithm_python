#include <iostream>
#include <unordered_set>
#include <unordered_map>

// unordered_map/Set
/*
 * Map과 Set은 내부 구조가 이진 탐색트리로 구성되어 자동으로 정렬되는 자료구조이다.
 * 정렬 상태가 필요하지 않는 경우 이러한 내부 정렬 프로세스가 불필요한 성능저하로 이루어질 수 있다.
 * C++에서는 unordered_map, unordered_set을 제공하여 기존 map, set과 동일한 방법으로 사용할 수 있다.
 */



using namespace std;

int main() 
{
  unordered_set<int> UnorderedSet;

  UnorderedSet.insert(3);
  UnorderedSet.insert(1);
  UnorderedSet.insert(4);
  UnorderedSet.insert(2);

  for (int num: UnorderedSet) {
    cout << num << " ";
  }
  cout << endl;

  unordered_map<string, int> UnorderedMap;

  UnorderedMap["apple"] = 3;
  UnorderedMap["banana"] = 1;
  UnorderedMap["cherry"] = 4;
  UnorderedMap["date"] = 2;

  for (const auto& pair: UnorderedMap) {
    cout << pair.first << ": " << pair.second << endl;
  }
  cout << endl;


  return 0;
}
