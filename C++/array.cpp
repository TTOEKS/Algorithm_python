#include <cstdint>
#include <iostream>
#include <ratio>

using namespace std;

/*
 * 배열
 *   - 같은 타입의 원소를 효율적으로 관리할 수 있는 자료형
 *   - 하나의 변수로 동일한 타입의 데이터들을 관리하고 인덱스로 접근
 *   - 2차원, 3차원 배열과 같이 다차원 배열을 사용하는 경우도 있음
 *     (다차원 배열 역시, 1차원 공간에 연속 할당)
 *
 * 배열의 효율
 *   - 배열은 임의의 접근 방법을 사용: 모든 위치의 데이터 한번에 접근 가능
 *     -> 데이터 접근 시간: O(1)
 *   - 데이터를 뒤에 추가할 때: O(1) / 데이터를 맨 앞/중간에 삽입: O(N)
 *                                     -> 기존 데이터들을 뒤로 한칸 씩 이동
 *
 * 배열 선택 시 고려사항
 * 데이터에 자주 접근하거나, 읽어야 하는 경우에 좋은 성능을 보임 (ex. 그래프 표현)
 * 1. 할당 가능한 메모리 크기 확인 필요
 *   - 표현하려는 데이터가 너무 많은 경우, 할당에 실패할 수 있음
 *   - 정수형 기준 보통: 1차원 배열 1,000만 개 / 2차원 배열: 3,000 * 3,000 개 
 *
 * 2. 중간에 데이터를 삽입하는 경우가 많은지
 *   - 배열은 선형 자료구조로 중간이나 처음에 데이터를 삽입할 때 성능 저하됨
 *   - 시간 초과로 해당 테스트에 실패할 수 있음

int main(int argc, char **argv) 
{
  // 배열 선언
  int arr1[] = {1, 2, 3, 4, 5};
  int arr2[5] = {1, 2};


  // int 배열의 주소값 (4 Byte 씩 주소 증가)
  cout << &arr1[0] << endl << &arr1[1] << endl << &arr1[2] << endl;
  // -> double: 8 byte / char: 1 byte 씩 증가
  
  // 2차원 배열
  int arr[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
  for (int i=0; i<3; i++) {
    for (int j=0; j<4; j++) {
      cout << arr[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}
*/



#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>

using namespace std;

void bubble_sort(vector<int> &v) {
  for (size_t i = 0; i < v.size() ; ++i) {
    for (size_t j = 0; j < v.size() - i - 1; ++j) {
      if (v[j] > v[j + 1])
        swap(v[j], v[j + 1]);
    }
  }
}

int main() 
{
  vector<int> vec(90000);
  for (int i = 0; i < 90000; i++) {
    vec[i] = i + 1;
  }

  vector<int> vecForBubbleSort = vec;
  clock_t startBubbleSort = clock();
  bubble_sort(vecForBubbleSort);
  clock_t endBubbleSort = clock();
  double timeBubbleSort = double(endBubbleSort - startBubbleSort) / CLOCKS_PER_SEC;

  vector<int> vecForSort = vec;
  clock_t startSort = clock();
  bubble_sort(vecForSort);
  clock_t endSort = clock();
  double timeSort = double(endSort - startSort) / CLOCKS_PER_SEC;

  cout << "버블 정렬 수행 시간: " << timeBubbleSort << " Sec" << endl;
  cout << "std::sort 수행 시간: " << timeSort << " Sec" << endl;

  return 0;

}

