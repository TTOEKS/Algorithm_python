"""
각 언어 별 동적 배열
  * python - list()
  * C++ - std::vector
  * JAVA - ArrayList

파이썬의 리스트
  * Stack, Queue에서 필요한 연산을 모두 제공
  * 모든 연산이 O(1) 시간 복잡도를 가짐
  * 단, 삭제 (pop())연산은 O(n)을 가짐 -> deque로 성능 개선 가능
  * 파이썬 리스트 정렬 list.sort()는 Timsort를 사용 (최선: O(n))


각 언어 별 해시 테이블
  * python - dict()
  * C++ - std::unordered_map
  * JAVA - HashMap

파이썬의 딕셔너리
  * Key-Value 구조로 이루어진 자료형
  * 내부적으로는 해시 테이블로 구현되어 있음
  * 모든 연산이 O(1)에 가능 / 최악의 경우 O(n)이지만, 분할 상황 분석에 따르면 O(1)

파이썬의 다양한 딕셔너리
  * collections.OrderedDict(): 순서가 유지되는 dict
  * collections.defaultdict(): 항상 디폴트 값을 생성해 키 오류 방지
  * collections.Counter(): 요소 값을 키, 개수를 값으로 카운팅하는 dict
"""

import collections


if __name__=="__main__":
    # Python List

    # LIST INSERT
    a = [1, 2, 3]
    a.append(4)
    a.insert(3, 5)

    # Multiple type in single list
    # 파이썬은 모든 것이 객체이며, 리스트 역시 객체에 대한 포인터
    # 파이썬 리스트는 연결 리스트에 대한 포인터 목록을 관리하기 때문에 가능
    a.append("Hello")
    a.append(True)

    # Slicing
    ## 1, 2
    print(a[1:3])

    # 1, 2, 3
    print(a[:1])

    # 4, 5, 6, 7
    print(a[3:])

    # 1, 3
    print(a[1:4:2])

    try:
        print(a[10])
    except IndexError:
        print("존재하지 않는 인덱스")


    # Python variable dict
    # default dict
    a = collections.defaultdict(int)
    a['A'] = 5
    a['B'] = 4
    a['C'] += 1  # No error (it has defualt value)

    a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
    b = collections.Counter(a)
    print(b)

    # python 3.7 부터 내부적으로 인덱스를 이용해 입력 순서 유지되도로 개선
    # 더 이상 OrderedDict는 사용이 불필요
    c = collections.OrderedDict({'banana':3, 'apple':4, 'pear':1})



