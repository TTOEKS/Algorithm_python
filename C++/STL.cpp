// STL (Standard Template Library)
/*
* C++에서 제공하는 템플릿 기반 표준 라이브러리이다.
* C++에서 함수나 클래스를 구현할 때, 어떤 타입에서도 동작할 수 있도록 하는 문법이다.
* STL은 크게 데이터를 담을 Container, 데이터를 처리하는 여러 Algorithm, 컨테이너 접근 및 순회 가능한 Iterator로 구성된다.
*/

// 상수 레퍼런스
/*
* C++에서는 함수의 인수로 값을 전달 할 때 값을 복사하여 전달한다. (Call by value)
* 함수의 인수로 값을 복사할 때 마다 복사 비용이 발생하여, 성능에 영향을 줄 수 있다.
*/

// STL Container
/*
 * STL의 컨테이너는 데이터를 저장할 수 있는 객체를 의미한다.
 * 많은 컨테이너를 지원하지만, 코딩 테스트에서는 주로 아래 컨테이너들을 자주 사용한다.
 * Container: vector, set, map, priroity queue
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void modify(int value) {
  value = 10;
  cout << "주소 " << &value << endl;
  cout << "값: " << value << endl;

  return ;
}

void call_by_value() {
  int value = 5;
  cout << "주소 " << &value << endl;
  cout << "값: " << value << endl;
  modify(value);
  cout << "값: " << value << endl;
  /*
    * Modify 함수 호출 시, 다른 공간에 value 변수가 생기고 인수로 전달한 값이 복사된다.
    * 즉, modify 함수의 value 변경은 call_by_name 함수의 value에 영향을 미치지 않는다.
    * modify()함수 호출 이후에도 call_by_name()함수 내 value는 5
    */
  return;
}

// Call by reference
/*
* 크기가 1,000만인 정수형 배열을 포함한 경우 큰 메모리를 복사하므로, 비용이 크게 발생할 수 있다
* 이런 경우, 객체 전체를 복사하지 않고, Reference를 활용하여 인수를 전달한다. (Call by reference)
* '&' 문법을 활용하여 변수 자체를 복사하지 않고, 참조자를 통해 변수에 직접 접근하여 수정할 수 있다.
*/

void modify(int& value) {
  void = 10;
  cout << "주소 " << &value << endl;
  cout << "값: " << value << endl;

  return ;
}

void call_by_reference() {
  int value = 5;
  cout << "주소 " << &value << endl;
  cout << "값: " << value << endl;
  modify(value);
  cout << "값: " << value << endl;

  /*
  * Modify 함수 호출 시, call_by_reference() 함수 내 value를 직접 참조하여 수정한다.
  * 즉, modify 함수의 value 변경이 call_by_reference 함수 내의 value에 영향을 미친다.
  * modify() 함소 호출 이후에 call_by_reference() 함수 내 value는 10
  */

  return;
}


// auto 문
/* 
* STL은 어떤 타입이라도 사용할 수 있도록 잘 구현되어 있다.
* 타입이 복잡해지는 경우, 실수, 코드 가독성 저하로 이어질 수 있다.
* auto 키워드를 호라용하면 변수의 타입을 자동으로 추론하기 때문에 더 간결하게 작성할 수 있다.
*/

void auto_keyword() {
  auto num = 42;
  cout << num << endl;

  auto pi = 3.14159;
  cout << pi << endl;

  auto greeting = string("Hello world");
  cout << greeting << endl;

  return; 
}


// 범위 기반 반복문
/* 
* 배열이나 컨테이너의 모든 원소를 순회할 때, 사용한다.
* 기존 반복문보다 구현이 쉽고, 가독성이 좋아진다.
*/

void range_based_loop() {
  vector<int> vec = {1, 2, 3, 4, 5};

  for (int num: vec) {
    cout << num << endl;
  }
  cout << endl;

  // STL 컨테이너와 사용할 때는 수정할 필요가 없어 auto 대신, 상수 래퍼런스를 적용한 const auto&를 사용
  // 컨테이너를 반복문으로 넘기거나, 함수 인자로 사용할 때 복사 비용을 고려해야 한다.
  map <string, int> fruitMap = {{"apple", 1}, {"banana", 2}, {"cherry", 3}};
  for (const auto& pair: fruitMap) {
    cout << pair.first << "=" << pair.second << " ";
  }
  cout << endl;

  set<string> fruitSet = {"apple", "banana", "cherry"};
  cout << "Set: ";
  for (const auto& fruit: fruitSet) {
    cout << fruit << " ";
  }
  cout << endl;

}
  return;
