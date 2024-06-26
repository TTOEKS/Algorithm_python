
"""
파이썬은 정렬함수를 기본적으로 제공한다.
  * 정렬 알고리즘은 Timsort 파이썬에서 시작된 정렬 알고리즘을 사용

Timesort
  * 팀 피터스가 파이썬을 위해 C로 구현한 정렬 알고리즘
  * 우아한 정렬보다는 실용적인 정렬 알고리즘
  * '실제 데이터는 대부분 이미 정렬되어 있을 것'이라는 가정 하에 동작
  * 삽입 정렬과 병합 정렬을 휴리스틱하게 적절히 사용한 것으로 알려짐
  * 현재는 Java, Swift, Android, Chrome 등 다양한 곳에서 포팅해 사용 중
  * GO의 경우 병합 정렬로 인한 공간 복잡도로 거절

Deep
정렬 알고리즘에서 인기 있는 알고리즘: Merge, Quick 
  * Quick 정렬은 Merge 정렬보다 더 빠르지만 데이터에 따라 편차가 있다.
  * Merge 정렬은 데이터에 덜 민감해 일정하게 O(n log n)성능을 보인다.
  * Merge 정렬은 안정 정렬 (Stable Sort) 특성을 가지고 있다.

"""

def comp_func(x):
    return x[0], x[-1]

if __name__=="__main__":

    ### 기본 정렬: 리스트, 문자, 문자열
    list_int = [2, 5, 1, 7, 9]
    sorted(list_int)

    list_ch = ['a', 'c', 'd', 'b', 'e']
    sorted(list_ch)

    string = "zbefqa"
    print("".join(sort(string)))


    ### 리스트 자료형에는 자체적인 Sort 함수가 존재하
    list_int_2 = [9, 3, 2, 1, 5]

    # 제자리 정렬: 입력을 출력값으로 덮어쓰기 때문에 추가 메모리 사용 X / 리턴 : None
    list_int_2.sort()


    ### Sorted Key
    # key= 옵션을 통해 정렬을 위한 키 또는 함수를 별도로 지정할 수 있다.
    c = ['ccc', 'bb', 'aaaaa', 'd']
    sorted(c, key=len)


    a = ['cde', 'cfc', 'abc']
    # 함수를 이용해 첫 문자와 마지막 문자 순으로 정렬
    sorted(a, key=comp_func)

    # 람다를 통해 한줄로도 표현 가능
    sorted(a, key=lambda x: (x[0], x[-1]))
    
    




