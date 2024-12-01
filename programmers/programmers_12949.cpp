#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    
    int num_cols = arr2.size();
    
    for (int i=0; i<arr1.size(); i++) {
        vector<int> tmp_vec;
        for (int j=0; j<arr2[0].size(); j++) {
            int sum = 0;
            for (int k=0; k<num_cols; k++) {
                sum += arr1[i][k] * arr2[k][j];
            }
            tmp_vec.push_back(sum);
        }
        answer.push_back(tmp_vec);
    }
    
    return answer;
}

vector<vector<int>> best_solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    
    answer.assign(arr1.size(), vector<int>(arr2[1].size(), 0));

    for (int i=0; i<arr1.size(); i++) {
        for (int j=0; j<arr2[1].size(); j++) {
            for (int k=0; k<arr2.size(); k++) {
                answer[i][j] += arr1[i][k] * arr2[k][j];
            }
        }

    }

    return answer;
}
