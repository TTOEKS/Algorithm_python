#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    
    for (int i=0; i<numbers.size(); i++) {
        for (int j=i + 1; j<numbers.size(); j++) {
            answer.push_back(numbers[i] + numbers[j]);
        }
    }
    sort(answer.begin(), answer.end());
    answer.erase(unique(answer.begin(), answer.end()), answer.end());
    
    return answer;
}

vector<int> best_solution(vector<int> numbers) {
    set<int> sum;
    
    for (int i=0; i<numbers.size(); i++) {
        for (int j=i + 1; j<numbers.size(); j++) {
            sum.insert(numbers[i] + numbers[j]);
        }
    }
    vector<int> answer(sum.begin(), sum.end());
    return answer;
}
