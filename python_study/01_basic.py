# Basic modules
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import pprint
import copy
from typing import *

"""
좋은 코딩 스타일을 위한 자료
JAVA
Clean Code (로버트C.마틴, 2013)

C LANG
프로그래밍 수련법 (브라이언 W.컨니핸, 2008)

PYTHON
PEP8 (www.python.org/dev/peps/pep-0008)
Google python style guide (google.github.io/styleguide/pyguide.com)


"""
# @staticmethod 데코레이터
"""
JAVA의 애노테이션 (Annotation)이라 불리는 것과 유사한 문자로 특히 static 선언과 유사하다
위 데코레이터가 정의된 메소드는 클래스와 독립적으로 함수로서 의미를 강하게 갖는다
즉, 클래스의 메소드가 아니라 독립된 함수의 의미를 가진다
-> 클래스 메소드처럼 자유롭게 클래스 인스턴스에 접근하는 것이 제한됨
"""
class CLASS:
    def a(self):
        pass

    @staticmethod
    def b():
        pass

"""
type(CLASS.a) -> function
type(CLASS.b) -> function

cls = CLASS()
type(cls.a) -> method
type(cls.b) -> function
"""


# PASS: 아무런 동작 안함 (인터페이스 목업에서 사용 가능)
class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B")


# Type hint는 명시적으로 힌트만 주는 것으로, 실제로는 동적할당으로 동작 #
# Type hint
def fn(a: int) -> bool:
    print(a)

    return True

# Generator yield
    # Return은 값을 리턴하고 해당 함수의 동작을 종료함
    # Yield는 중간값을 리턴한 다음 함수를 종료하지 않고 계속 실행
    # 제너레이터 관련해서는 조금더 공부해야 할 듯

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

if __name__=="__main__":
    ########## TYPE HINT
    type_hint_a: str = "1"
    type_hint_b: int = 1


    ########## LAMBDA
    # lambda 

    lambda_c = list(map(lambda x: x + 10, [1, 2, 3]))

    ########## LIST COMPRESS
    list_a = []
    for n in range(1, 10 + 1):
        if (n % 2 == 1):
            list_a.append(n * 2)

    # List compression
    list_b = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]

    original = {"Key": "value"}
    dict_a = {}
    for key, value in original.items():
        dict_a[key] = value

    # dictionary compression
    dict_b = {key: value for key, value in original.items()}


    ########## GENERATOR
    g = get_natural_number()

    for _ in range(0, 100):
        # next() 함수로 제너레이터 값 추출
        print(next(g))


    ########## RANGE -> class
    list(range(5))
    # [0, 1, 2, 3, 4]

    # RANGE 1
    # 이미 값을 생성해서 메모리에 올려둔 상태
    range_a = [n for n in range(100000)]

    # RANGE 2
    # 생성해야 한다는 조건만 넣어둔 상태
    range_b = range(100000)
    # 2번은 1번에 비해서 메모리 사용률이 매우 적고, 인덱스로도 접근 가능


    ########## ENUMERATE (열거하다)
    # 리스트의 인덱스를 자동으로 할당해주는 객체

    a = ['a', 'b', 'c']
    for i in range(len(a)):
        print(i, a[i])

    for i, v in enumerate(a):
        print(i, v)


    ########## print
    print("A1", "B2")
    print("A1", "B2", sep=",")
    print("A1", "B2", end="")

    idx = 1
    fruit = "apple"
    print("{0}: {1}".format(idx + 1, fruit))
    print("{}: {}".format(idx + 1, fruit))
    print("f{idx + 1}: {fruit}")


    c = MyClass()


    ########## locals: 로컬 심볼 테이블 딕셔너리 반환
    # 로컬에 선언된 모든 변수를 조회
    pprint.pprint(locals())


    ########## GOOD LIST COMPRESSION
    str1 = "test1234test"
    # BAD
    str1s = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i + 2].lower())]

    # NOT BAD
    str2s = [
        str1[i:i + 2].lower() for i in range(len(str1) -1)
        if re.findall('[a-z]{2}', str1[i:i + 2].lower())
    ]
    
    # COOL
    for i in range(len(str1) - 1):
        if re.findall('[a-z]{2}', str1[i:i + 2].lower()):
            str1s.append(str1[i:i + 2].lower())


    ########## GOOGLE PYTHON STYLE GUIDE (가독성)
    """
    YES
    if not users:
        print('no users')

    if foo == 0:
        self.handle_zero()

    if i % 10 == 0:
        self.handler_multiple_of_ten()

    NO
    if len(users) == 0:
    print('no users')

    if foo is not NOne and not foo:
        self.handle_zero()

    if not i % 10:
        self.handler_multiple_of_ten()
    """

    # Zip() 함수와 아스테리스크 (*)

    """
    zip(): zip 함수는 iter 가능한 객체 인자를 받아 원소들을 튜플 형태로 반환
      * 중복되지 않은 튜플 시퀀스를 생성
    """

    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd']
    c = ['A', 'B', 'C']
    zip(a, b, c)
    #[(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C')

    a = ['a1', 'a2']
    b = ['b1', 'b2']
    c = ['c1', 'c2']
    d = ['d1', 'd2']
    zip(a, b, c, d)
    #[('a1', 'b1', 'c1', 'd1'), ('a2', 'b2', 'c2', 'd2')

    """
    아스테리스크 (*)
    파이썬에서 아스테리스크 (*)는 Unpack 동작을 수행한다
      * 시퀀스 언패킹 연산은 스퀀스를 풀어헤치는 연산자를 뜻함
      * 주로, 튜플이나 리스트를 언패킹하는데 사용
      * (*) 1개는 주로 튜플 또는 리스트 등의 시퀀스 언패킹 / (*) 2개는 키/값 언패킹에 사용
    """

    fruit = ['apple', 'banana', 'melon', 'kiwi']
    for f in fruit:
        print(f)

    print(*fruit)

    date_info = {'year':'2020', 'month':'01', 'day':'7'}
    new_info = {**date_info, 'day':'14'}
    

    """
    중첩 함수: 함수 내에 위치한 또 다른 함수
      * 부모 함수의 변수들을 자유롭게 읽을 수 있음
      * 자주 사용되지는 않지만, 단일 함수로 문제를 해결해야 하는 곳에서 사용됨
    """

    # 연산자 조작
    def outer_func(a: List[int]):
        b: List[int] = a
        print(id(b), b)

        def inner_func_1():
            b.append(4)
            print(id(b), b)

        def inner_func_2():
            print(id(b), b)

        inner_func_1()
        inner_func_2()

    outer_func([1, 2, 3])
    # Result: All function call's varible ID is same

    # 재할당
    def outer_func_realloc(t: str):
        text: str = t
        print(id(text), text)

        def inner_func_realloc_1():
            text = 'world'
            print(id(text), text)

        def inner_func_realloc_2():
            print(id(text), text)

        inner_func_realloc_1()
        inner_func_realloc_2()

    outer_func_realloc("Hello!")
    # Result: 오직 inner_func_realloc_1 함수에서만 text 값이 변하고, id도 다른 변수가 됨
    # (=) 연산자로 변수를 새롭게 할ㄷ아하는 경우, ID 값이 변경되어 서로 다른 변수가 됨
    # 자식 함수에서 재할당한 변수는 로컬변수가 되어 부모변수까지 반영 안됨
    # list 혹은 dictionary의 경우 append() 메소드를 통해 재할당 없이 조작 가능
    # 숫자, 문자 자료형과 같은 불변 객체의 경우 재할당이 발생해 중첩함수 내에서 변경 불가


    # 객체 복사
    """ 
    파이썬의 중요한 특징 중하나는 모든 것이 객체라는 점이다.
      * 숫자, 문자 까지도 모두 객체이고, 딕셔너리, 리스트와 차이점은 불변 객체라는 점
      * 별도로 값을 복사하지 않는 한, 변수에 값을 할당하는 것은 값 객체를 참조하는 것
    """

    copy_a = [1, 2, 3]
    b = a
    c = a[:]
    d = a.copy()
    print(id(a), id(b), id(c), id(d))
    # a와 b는 같은 객체를 참조, c와 d는 다른 객체
    # 중첩 리스트를 복사하기 위해서는 deepcopy()를 사용해야 함

    multi_list_copy_a = [1, 2, [3, 5], 4]
    b = copy.deepcopy(a)
    print(id(a), id(b), b)

    # (,) 콤마 연산자
    a = [1]
    b = [2, 3]
    a += b
    # a = [1, 2, 3]
    a += b,
    # a = [1, [2, 3]]

    # 재귀 제한
    """
    파이썬에는 재귀 호출에 대한 호출 횟수 제한이 있으며, 기본 값은 1,000으로 설정되어 있음
    sys.getrecursionlimit() -> 1000
    """

    # 속도 테스트
    """
    timeit -n 10000 bisect.bisect_left(a, 5)
    timeit -n 10000 a.index(5)
    """


    # any(), all() 함수
    """
    any() 함수는 포함된 값 중 어느 하나가 참이라면 항상 참을 출력 (OR)
    all() 함수는 모든 값이 참이어야 True를 출력 (AND)
    """
