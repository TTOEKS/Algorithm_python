# Deque and priority queue
"""
Deque
  * Double ended queue의 줄입말로, 양쪽 모두 추출이 가능한 큐를 의미함
  * 양쪽에서 삭제, 삽입을 모두 처리할 수 있음
  * Stack, Queue의 특징을 모두 가지고 있음
  * ADT 구현은 Array, Linked-List로 가능하지만, Doubly-Linked-List로 구현하는게 가장 알맞음

Priority Queue
  * 우선순위 큐는 큐 또느 스태과 같은 추상 자료형과 유사
  * 하지만, 각 요소의 '우선순위'가 존재한다는 점이 있음
  * 특정한 조건에 따라 우선순위가 가장 높은 요소가 추출 됨
  * Dijkstra Algorithm, Heap 자료구조와 관련도가 높음

python의 Pirority Queue 자료형
  * python은 우선순위 큐 구조를 위해 PriorityQueue, heapq 2가지 자료형을 지원한다
  * 내부적으로 확인하면 PriorityQueue가 heapq를 사용하므로, 동작 차이점은 없음
  * 두 자료 간 차이점은 Thread-Safe를 지원하는가 아닌가 임
    * heapq 모듈은 Thread-Safe 보장을 하지 않음
    * PriorityQueue 모듈은 Thread-Safe를 보장
  # heapq의 heappush(list, items) 인데 itmes 인자에 여러 값이 (data1, data2, ..) 처럼 튜플로 입력된 경우 첫번째 인자 (data1)을 기준으로 정렬한다. *

Thread-Safe
  * 멑리 스레드에서도 안전한 동작을 보장하는 가?
  * Thread-Safe가 확보되지 않은 두 스레드에서는 1번 스레드의 값이 2번 스레드에서 변경될 수 있음

heapq가 PriorityQueue 보다 많이 사용되는 이용되는 이유
  * python은 GIL의 특성상 멀티 스레딩이 거의 의미가 없음
  * Thread-safe를 보장하는 것은 내부적으로 Locking 동작이 있다는 것
  * Locking Overhead가 발생해 성능에 영향을 줄 수 있음

파이썬 전역 인터프리터 락 (GIL: Global Interpreter Lock)
  * 파이썬 최초 구현체인 CPython은 개발 초기 아래와 같은 문제를 관리하기 우해 GIL로 파이썬 객체에 대한 접근을 제한하는 형태로 설계함
    * 번거로운 동시성 관리
    * 스레드 세이프하지 않은 CPython의 메모리 관리
  * 하나의 스레드가 자원을 독접하는 형태로 실행 됨
  * 최초 개발 당시는 CPU가 하나였기 때문에 이러한 개념이 이해가 됨
  * 멀티 Core가 지원하는 현재는 이러한 개념이 python은 성능이 느리다라는 위명을 생기게 하였음
  * 현재 GIL을 사용하지 않기 위해 시도 중이지만, 과거부터 GIL에 의존해 개발되 힘들다
"""


if __name__=="__main__":
    print("Hello World")
