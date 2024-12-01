/*
 * Built In 데이터 타입
 * C++에서 많이 사용하는 빌트인 데이터 타입은 아래와 같음
 *   - 정수형 (int)
 *   - 부동소수형 (float or double)
 *   - 논리형 (Bool)
 *   - 문자형 (char)
 *
*/

#include <iostream>
#include <string>

using namespace std;

// 정수형
/*
* 정수형은 양의 정수, 음의 정수 0을 포함한다.
*   - 정수형은 더하기, 빼기, 곱하기, 나누기 등 사칙 연산 가능
*
* AND, OR 연산
*   - AND 연산 -> 직렬 연산: 모든 스위치가 닫혀야 동작
*   - OR 연산 ->  병렬 연산: 하나의 스위치라도 닫히면 동작
*/
void int_test() {
  int a = 13;
  int b = 4;

  // 정수형 사칙 연산
  cout << a + b << endl;
  cout << a - b << endl;
  cout << a * b << endl;
  cout << a / b << endl;
  cout << a % b << endl;

  // 정수형 비교 연산
  cout << (a == b) << endl;
  cout << (a != b) << endl;
  cout << (a > b) << endl;
  cout << (a < b) << endl;
  cout << (a >= b) << endl;
  cout << (a <= b) << endl;

  // 정수형 비트 연산
  cout << (a & b) << endl;
  cout << (a | b) << endl;
  return;
}

// 부동 소수형
/*
* 부동 소수형은 소수를 저장할 떄 사용한다.
*   - C++에서 부동 소수형은 float, double 형태가 있음
*   - doulbe은 8 byte 자료형 (15자리), float는 4byte 자료형 (7자리)
*/

void float_test() {
  double d = 2.5;
  float f = 1.5f;

  cout << sizeof(d) << endl;
  cout << sizeof(f) << endl;
  cout << d << " "<< f << endl;
  cout << d + f << endl;
  cout << d - f << endl;
  cout << d * f << endl;
  cout << d / f << endl;
  return;
}

// 형 변환
/*
* C++은 변수를 선언하는 순간 타입이 정해진다.
* 구현 중, 타입을 변경해야 할 상황이 오면 형 변환을 해주어야 한다.
* 서로 다른 타입의 변수간 연산을 통해 발생하며, 아래 2가지 변환이 존재한다.
*   - 암시적 형 변환 (Implicit conversion)
*   - 명시적 형 변환 (Explicit conversion)
* 보통 암시적 변환은 변수의 메모리 크기가 큰 쪽으로 변환됨
* ex) 정수형(4 byte) <-> 부동소수형(8 byte) -형변환-> 부동소수형
*/

void type_conversion() {
  int i = 65;
  float f = 5.2f;

  // 암시적 형변환 (float로 변환)
  double d = i * f;
  cout << d << endl;

  // 명시적 형 변환
  cout << static_cast<int>(d) << endl;
  cout << static_cast<char>(i) << endl;

  return;
}

// 문자열
/*
* C++에서는 문자열 자료형을 제공하는데, string 표준헤더를 추가해 사용 가능하다.
*   - 문자열 작업을 쉽고 효율적으로 할 수 있는 다양한 메서드 제공
*/

void string_func() {
  // 빈 문자열 선언
  string str1;
  // 문자열 직접 초기화
  string str2 = "Hello, world!";
  // 문자열 복사
  string str3(str2);
  // 문자열 부분 복사 -> Hello
  string str4(str2, 0, 5);
  // 반복된 문자로 문자열 초기화
  string str5(10, '*');

  // 문자열 찾기
  string str = "Hello, C++ World!";

  size_t pos1 = str.find("Hello");
  cout << pos1 << endl;

  size_t pos2 = str.find('C');
  cout << pos2 << endl;

  size_t start_index = 2;
  size_t pos3 = str.find("Hello", start_index);
  cout << pos3 << endl;

  size_t pos4 = str.find("Python");
  cout << pos4 << endl;
  // pos3, pos4는 쓰레기 값을 출력하는데, 검색에 실패해서 그렇다.
  // 해당 값은 환경마다 다르며, string::npos 값이라고 볼 수 있음
  
  // 문자열 추가, 수정
  string tmp = "APPLE";
  str += ", World!";
  cout << tmp << endl;

  str[7] = 'P';
  cout << tmp << endl;

  // 보통 replace는 문자열 길이가 N일 때 O(N)만큼의 시간이 걸림
  // 7번째 문자부터 'Col'로 변경
  str.replace(7, 4, "Col");
  cout << tmp << endl;

  return ;
}


int main() 
{
  int_test();
  
  return 0;

}
