## Code up Site 1099: 먹이 찾는 개미
## Program ID: codeup_1099.py

'''
미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)
'''

def display_board():
    for i in range(10):
        for j in range(10):
            print(board[i][j], end=" ")
        print()


board = [[0 for col in range(10)] for row in range(10)]

for i in range(10):
    board[i] = list(map(int, input().split()))

'''
개미집 2, 2

1. 오른쪽에 먹이가 있는가? -> 오른쪽으로 이동 후 종료
2. 오른쪽에 길이 있는가?   -> 오른쪽 이동
2. 없다면 밑으로           -> 아래로 이동
4. 만약 먹이를 찾지 못하고 끝에 다다를 경우 그 자리에서 멈춤
0: 길, 1: 벽 2: 먹이 9: 개미 이동 경로

while(!(ant[x][y] == 2)):

'''

# init ant place
x = 1
y = 1


while(board[y][x] != 2 and x != 9 and y != 9):
    board[y][x] = 9
    
    if(board[y][x+1] == 0):
        x+=1
    elif(board[y][x+1] == 2):
        x+=1
        break
    else:
        y+=1

# ant find feed
if(x != 9 and y != 9):        
    board[y][x] = 9


display_board()


'''
Exam)
input:
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

output:
1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
