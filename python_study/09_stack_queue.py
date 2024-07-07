
"""
Stack과 Queue는 고전적이지만, 많이 사용되는 자료구조이다.
  * Stack은 LIFO (Last-In-First-Out, 후입선출) 특성을 가짐
  * Queue는 FIFO (First-In-First-Out, 선입선출) 특성을 가짐

Python은 Stack, Queue 자료형을 별도로 제공하지 않음
  * List 자료형이 Stack, Queue 연산 모두 가능
  * List 자료형은 동적 배열로 구현되어 Queue 연산으로는 효율적이지 못함
  * Queue의 효율성을 위해서는 Deque 자료형을 사용
  * 효율성을 따지지 않는다면 Stack, Queue 모두 List로 구현 가능

Stack은 아래 2가지 주요 연산을 지원하는 요소의 Collection으로 사용되는 추상자료형이다.
  * push(): 요소를 Collection에 추가
  * pop(): 아직 제거되지 않은 가장 최근 삽입된 요소를 제거

Stack의 역사는 앨런 튜링에서 시작된다.
  * 서브루틴 호출하는 과정에서 Stack이 기원됨
  * Stack은 Call Stack이라 하여 컴퓨터 프로그램의 서브루틴에 대한 정보를 저장하는 자료구조에 활용
    ex) Compiler의 Call Stack 에러에서 스택 구조 확인 가능
  * 메모리 영역에서 LIFO 형태로 할당/접근하는 구조인 아키텍처 레벨의 하드웨어 스택의 요소에서도 사용

Queue
  * 시퀀스의 한쪽 끝에서 엔티티를 추가하고, 반대쪽에서 엔티티가 제거되는 엔티티 컬렉션
  * FIFO (First-In-First-Out, 선입선출)로 처리되는 자료구조
  * Deque, Priority-Queue 등 다양한 분야에서 유용하게 사용됨
  * 우선 탐색 (BFS), 캐시 (Cache) 등을 구현할 떄도 사용

Circular Queue (원형 큐)
  * FIFO를 가진다는 점에서 기존 큐와 동일
  * 마지막 위치가 시작위치와 연결되는 성질이 있어 원형 구조를 가짐
  * 마지막 위치와 시작 위치가 있고 이 두 포인터가 움직임
  * rear(뒤), front(앞) 두 위치가 동일한 경우 queue가 꽉 찬 

"""

# Implemented Stack using linkedlist (ADT)
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    for _ in range(5):
        print(stack.pop())

