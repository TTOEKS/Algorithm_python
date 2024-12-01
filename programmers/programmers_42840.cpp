#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int grade_first(vector<int> answers) {
    int res = 0;
    int guess_sheet[5] = {1, 2, 3, 4, 5};
    int guess = 0;
    
    // 1, 2, 3, 4, 5, 1, 2, ...
    for (int i=0 ; i<answers.size(); i++) {
        if (guess_sheet[(i%5)] == answers[i])
            res++;
    }
    return res;
}

int grade_second(vector<int> answers) {
    int res = 0;
    int guess_sheet[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    
    // 2, 1, 2, 3, 2, 4, 2, 5, ...
    for (int i=0 ; i<answers.size(); i++) {
        if (guess_sheet[(i%8)] == answers[i])
            res++;
    }
    return res;
    
}

int grade_thrid(vector<int> answers) {
    int res = 0;
    int guess_sheet[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    // 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    for (int i=0; i<answers.size(); i++) {
        if (guess_sheet[(i%10)] == answers[i])
            res++;
    }
    
    return res;
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int first_grades = 0;
    int tmp;
    
    tmp = grade_first(answers);
    if (tmp > first_grades)  {
        first_grades = tmp;
        answer.push_back(1);
    } else if (tmp == first_grades) 
        answer.push_back(1);
        
    tmp = grade_second(answers);
    if (tmp > first_grades)  {
        answer.clear();
        first_grades = tmp;
        answer.push_back(2);
    } else if (tmp == first_grades) 
        answer.push_back(2);
     
    tmp = grade_thrid(answers);
    if (tmp > first_grades)  {
        answer.clear();
        first_grades = tmp;
        answer.push_back(3);
    } else if (tmp == first_grades) 
        answer.push_back(3);
        
    return answer;
}

vector<int> firstPattern = {1, 2, 3, 4, 5};
vector<int> secondPattern = {2, 1, 2, 3, 2, 4, 2, 5};
vector<int> thirdPattern = {3, 3, 1, 1, 2, 2, 4, 4 ,5, 5 };

vector<int> best_solution(vector<int> answers) {
    vector<int> answer;

    vector<int> matchCnt(3);
    for (int i=0 ;i<answers.size(); i++) {
        if (answers[i] == firstPattern[i % firstPattern.size()])
            matchCnt[0]++;

        if (answers[i] == secondPattern[i % secondPattern.size()])
            matchCnt[1]++;

        if (answers[i] == thirdPattern[i % thirdPattern.size()])
            matchCnt[2]++;
    }

    int max_score = *max_element(matchCnt.begin(), matchCnt.end());

    for (int i=0; i<3; i++) {
        if (matchCnt[i] == max_score)
            answer.push_back(i + 1);
    }

    return answer;
}
