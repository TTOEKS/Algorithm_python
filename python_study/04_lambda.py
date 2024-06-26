"""
람다 표현식: 식별자 없이 실행 가능한 함수
  * 함수 선언 없이 하나의 식으로 함수 표현 가능
  * 람다 표현식은 코드를 간결하게 만들어 줄 수 있음
  * 람다 표현식은 코드의 가독성을 저하시키기 때문에 사용을 지양하는 것이 좋음
"""

import collections


def comp_func(x):
    return x.split()[1], x.split()[0]

if __name__=="__main__":
    s = ['2 A', '1 B', '4 C', '1 A']

    sorted(s)
    # ['1 A', '1 B', '2 A', '4 C']

    sorted(s, key=comp_func)
    # ['1 A', '2 A', '1 B', '4 C']

    sorted(s, key=lambda x:(x.split()[1], x.split()[0]))
    # ['1 A', '2 A', '1 B', '4 C']



