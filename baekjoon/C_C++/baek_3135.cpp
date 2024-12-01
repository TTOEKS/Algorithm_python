#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int comp(int a, int b) {
  return a > b;
}

int main(int argc, char **argv)
{
  int A, B, N;
  vector<int> move_to;

  cin >> A >> B >> N;
  move_to.push_back(A);
  int tmp;
  for (int i=0; i<N; i++) {
    cin >> tmp;
    move_to.push_back(tmp);
  }
  sort(move_to.begin(), move_to.end(), comp);


  return 0;
}

