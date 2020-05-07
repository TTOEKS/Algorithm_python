## Code up Site 1097:[2차원 배열] 바둑알 십자 뒤집기
## Program ID: Cross Reverse game
'''
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.
'''

array = [[]*19]*19

def reverse(a, x, y):
    # x pivot reverse
    for i in range(19):
        if(a[x-1][i] == 0):
            a[x-1][i] = 1
        else:
            a[x-1][i] = 0

    # y pivot reverse
    for i in range(19):
        if(a[i][y-1] == 0):
            a[i][y-1] = 1
        else:
            a[i][y-1] = 0
            

for i in range(19):
    array[i] = list(map(int, input().split()))

num = int(input())
switch = [[]*2]*num

for i in range(num):
    switch[i] = list(map(int, input().split()))
    reverse(array, switch[i][0], switch[i][1])

# display board
for i in range(19):
    for j in range(19):
        print(array[i][j], end=" ")
    print()


