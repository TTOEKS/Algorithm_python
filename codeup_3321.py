## Code up Site:3321 [Best Pizza]
## Program ID: codeup_3321.py

'''
vega teacher's favorite pizza store name is Miss pizza
he save a his money so he want get max calories of a dallor
피자 가게에서 주문할 수 있는 피자 중 1 달러 당 열량이 최대가 되는 피자를 주문하자.

첫 번째 줄에는 토핑 종류 수를 나타내는 하나의 정수 N (1 ≦ N ≦ 100)이 입력된다.
두 번째 줄에는 두 개의 정수 A, B (1 ≦ A ≦ 1000,1 ≦ B ≦ 1000)가 공백을 구분으로 입력된다. A는 도우의 가격, B는 토핑의 가격을 나타낸다.
세 번째 줄에는 도우의 칼로리를 나타내는 정수 C (1 ≦ C ≦ 10000)가 입력된다.
3 + i 행 (1 ≦ i ≦ N)는 i 번째의 토핑 칼로리 수를 나타내는 정수 Di (1 ≦ Di ≦ 10,000)가 입력된다.

이 중 최고의 피자의 열량을 계산하라
'''
def sort_array(a):
    count = len(a)
    for i in range(count-1, -1, -1):
        for j in range(i):
            if(a[j] < a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                
total_top_cal = 0

num = int(input())
top_cal = []


dou_price, top_price = input().split()
dou_price = int(dou_price)
top_price = int(top_price)

dou_cal = int(input())

for i in range(num):
    top_cal.append(int(input()))
    total_top_cal += top_cal[i]

# sorted topping calories big
sort_array(top_cal)

total_price = dou_price
total_cal = dou_cal

result_rate = total_cal//total_price

for i in range(num):
    total_price += top_price
    total_cal += top_cal[i]

    temp_result = total_cal//total_price

    if(temp_result>=result_rate):
        result_rate = temp_result
    else:
        break
print(result_rate)
