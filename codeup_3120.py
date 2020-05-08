# Code up Site: 3120 (온도조절)
# Program ID codeup_3120.py

'''
현재 온도와 목표 온도가 입력된다.
최소한의 버튼 사용으로 목표 온도가 되는 버튼 횟수를 출력하라

버튼 종류
1) 온도를 1도 올리는 버튼
2) 온도를 1도 내리는 버튼

3) 온도를 5도 올리는 버튼
4) 온도를 5도 내리는 버튼

5) 온도를 10도 올리는 버튼
6) 온도를 10도 내리는 버튼

그리디 알고리즘 사
'''

src_temp, dst_temp = input().split()
src_temp = int(src_temp)
dst_temp = int(dst_temp)

gap = dst_temp - src_temp
cnt = 0

while(gap!=0):
    '''
    Why am i set range like that
    10 = -10

    9 = -5 -1 -1 -1 -1
    9 = -10 +1

    8 = -5 -1 -1 -1
    8 = -10 +1 +1
    
    7 = -5 -1 -1
    7 = -10 +1 +1 +1
    8일 경우도 -10을 한 후에 조정하는 것이 cnt 값이 더 작다. 
    '''
    if(gap >= 8):
        gap -= 10
    elif(gap <= -8):
        gap += 10
    elif(gap >= 4):
        gap -= 5
    elif(gap <= -4):
        gap += 5
    elif(gap >= 1):
        gap -= 1
    elif(gap <= -1):
        gap += 1

    cnt += 1
    print(gap)
    
print(cnt)
