## 원숭이들을 두 개의 우리에 합사해라
## Program ID codeup_4763.py


'''
앙숙 관계인 원숭이들이 많다.
    하지만 한 원숭이에 대해 앙숙 관계에 있는 원숭이들의 수는 세 마리 이하이다.

동물원의 앙숙 관계를 조사하여 두 조건을 만족하도록 원숭이를 두 개의 우리에 나누어 수용하자
    Con1) 각 원숭이에 대해 같은 우리 안에 있으며 앙숙 관계인 원숭이는 한 마리 이하이다.
    Con2) 비어있는 우리는 없다.
    
'''
cage_1 = []
cage_2 = []
monkey_num = int(input())
# index = 0: num, 1, 2, 3, ... : relatvie
monkey_rel = [[] for idx in range(monkey_num)]

# Init: all monkey input cage 1
for i in range(monkey_num):
    monkey_rel[i] = list(map(int, input().split()))
    cage_1.append(i+1)

def solution():
    result = False
    count = 0
 
    # Check Cage 1
    for i in range(len(cage_1)):
        comp = cage_1.pop(0)-1
        # Move monkey
        if(check_rel(1, comp)):
            cage_2.append(comp+1)
            count += 1
        else:
            cage_1.append(comp+1)
            
    # Check Cage 2
    for i in range(len(cage_2)):
        comp = cage_2.pop(0)-1
        # Move monkey
        if(check_rel(2, comp)):
            cage_1.append(comp+1)
            count += 1
        else:
            cage_2.append(comp+1)

    if(count == 0):
        result = True
    return result


# If monkey_rel > 1, return True else return False
def check_rel(num, idx):
    count = 0
    if(num == 1):
        for i in range(monkey_rel[idx][0]):
            if(monkey_rel[idx][i+1] in cage_1):
                count += 1
    else:
        for i in range(monkey_rel[idx][0]):
            if(monkey_rel[idx][i+1] in cage_2):
                count += 1

    if(count <= 1):
        return False
    else:
        return True


while(True):
    if(solution()):
        break
cage_1.sort()
cage_2.sort()
for i in cage_1:
    print(i, end=" ")
print()
for i in cage_2:
    print(i, end= " ")

'''
Input:
5
3 2 3 4
3 1 3 5
3 1 2 4
3 1 3 5
2 2 4

Output:
1 3 5 
2 4 

'''
