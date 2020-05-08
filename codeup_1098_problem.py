## 설탕과자 뽑기 문제
## Program ID: codeup_1098_problem.py

'''
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

Exam)
input:
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5


output:
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''


# Code start
w, h = input().split()

w = int(w)
h = int(h)
array = [[0]*w]*h

num = int(input())
result  = [[]*4]*num



for i in range(num):
    result[i] = list(map(int, input().split()))
    
    # 0:length 1:direction 2, 3: (x, y)
    for j in range(result[i][0]):

        if(result[i][1] == 0):
            array[result[i][2]-1][result[i][3]+j-1] = 1;
        else:
            array[result[i][2]+j-1][result[i][3]-1] = 1;

for i in range(w):
    for j in range(h):
        print(array[i][j], end=" ")
    print()


