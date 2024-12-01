#include <iostream>
#include <vector>

using namespace std;


// Early return (조기 반환)
//  함수 실행 과정 중 함수의 끝에 도달하기 전 반환하는 것
//  코드 가독성 증가, 예외 처리 강화

double total_price(int quantity, double price) {
  double total = quantity * price;
  if (total > 100) {
    return total * 0.9;
  }

  /*
   * ~~~
  */
  return total;
}


// Guard clauses (보호 구문)
//  본 로직 시작 전에 예외 처리 구문을 추가하는 것
//  입력값에 대한 예외 고려 
double get_avg (const vector<int>& arr, int N) {
  if (arr.empty()) {  
    return -1;
  }

  if (N == 0) {
    return -1;
  }
  //...
  return 0.1;
}


int main(int argc, char **argv)
{

}
