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
    


    
    
