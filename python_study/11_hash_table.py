# Hash Table
"""
Hash table / Hash map
  * 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형 (ADT)를 구현하는 자료구조이다.
  * 대부분의 연산이 분할 상환 분석에 따른 시간 복잡도가 O(1)
  * 데이터의 양에 관계없이 빠른 성능을 기대할 수 있음

Hash
  * Hash Function: 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수
    ex) HashFunction: H(a) / H("ABCD") = A1, H("ABCE") = A2, ...

Hashing
  * Hash Table을 인덱싱하기 위해 Hash Function을 사용하는 것을 해싱(Hashing)이라고 한다.
  * 정보를 가능한 빠르게 저장하고 검색하기 위한 기법
  * Symbol table, Checksum, Loss function, Randomization function, 암호 등과 연관

성능 좋은 Hash function
  * 해시 함수 값 충돌 최소화
  * 쉽고 빠른 연산
  * 해시 테이블 전체에 해시 값이 균등하게 분포
  * 사용할 키의 모든 정보를 이용해 해싱
  * 해시 테이블 사용 효율이 높음

생일 문제 (Birthday Problem)
  * 생일의 가짓수는 윤년 제외 365개의 경우가 있음
  * 비둘기 집 원리 (Pigeonhole Principle)에 따라 366명 이상이 모여야 같은 생일이 나옴
  * 실제로는 23명만 모여도 50%가 넘고, 57명이 모이면 99%를 넘음
  * 이는 일반적인 상식 보다 충돌이 생각보다 쉽게 발생한다는 것릉 의미함

비둘기집 원리 (Pigeonhole principle)
n개의 아이템을 m개의 컨테이너에 넣을 때, n > m인 경우 적어도 하나의 컨테이너에 반드시 2개이상의 아이템이 들어감

로드 팩터 (Load factor)
해시테이블에 저장된 데이터 개수 n을 버킷수 k로 나눈 것
  * 로드팩터 비율에 따라서 해시 함수를 최적화 할지, 테이블 크기를 조절할지 결정
  * 해시 함수가 키들을 잘 분산해주는 비율을 나타내기도 함
  * 일반적으로 로드 팩터가 증가할 수록 해시 함수 성능이 저하 됨
  * JAVA의 경우 Default 0.75에서 이를 넘어선 경우, 동적 배열 처럼 해시 테이블 공간을 재할당

해시 함수
  * 해시 테이블을 인덱싱하기 위해 해시 함수를 사용하게 됨
  * 해싱에는 다양한 알고리즘이 있음
  * 가장 단순한 방법은 정수형 해싱 기법인 모듈로 연산을 통해 나머지를 사용하는 것
    * h(x) = x mod m
    * Magic number라 불리는 31은 메르센 소수 (2의 거듭제곱에서 1이 모자란 수)라고도 불림
    * Magic number는 JAVA의 해시함수 구현에 사용되었음

충돌 대응 (Collision)
  * 해시를 사용하다보면 충돌이 발생할 수 밖에 없는데 이를 해소하기 위한 대표적인 방법을 소개
  1. 체이닝 (Chainging)
    * 충돌이 발생한 경우 Linked List로 연결하는 방식
    * 구현이 쉬워 인기가 높은 편
    * 탐색이 O(1)이지만 최악의 경우 O(n)이
    * 최적화를 위해 데이터가 많아진 경우 Red-Black Tree를 사용하기도 함

  2. 오픈 어드레싱 (Open Addressing)
    * 탐사를 통해서 빈 공간을 찾아서 값을 할당
    * 선형 탐사의 경우 충돌 위치에서 순차적으로 빈 공간을 탐사
    * 선형 탐사의 경우 데이터들이 고르게 분포하지 않고 연속될 수 있음
    * 해시 테이블 연속된 데이터 그룹이 생기는 현상을 클러스터링 (Clustering)이라고 함

  * 다양한 언어들은 각자의 특성에 맞는 방식을 취함 
  * Chaining은 추가 메모리가 필요하며 이는 성능을 저하 시킬 수 있음
  * Addressing은 특정 충돌 횟수가 넘어가면 급격하게 성능이 저하됨
"""

import random

TRAILS = 100000
same_birthday = 0

def birthday_problem():
    global same_birthday
    for _ in range(TRAILS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthday += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthday / TRAILS * 100}%")



if __name__=="__main__":
    print("HEllo world")
    print("BIRTHDAY PROBLEM TEST")
    birthday_problem()

