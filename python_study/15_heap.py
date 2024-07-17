"""
힙 (heap)
  * 힙의 특성 (최소힙: 부모가 항상 자식보다 작거나 같음)을 만족하는 거의 완전한 이진트리
  * 오해 1: 힙은 정렬된 구조가 아니라는 것
  * 힙은 유용한 자료구조로, 다양한 곳에서 활용 된다.
    * 우선순위 큐, 다익스트라 알고리즘, 힙 정렬, 최소 신장 트리, 프림 알고리즘, 중앙값의 근사값 계산...

힙(heap) vs 이진탐색트리 (BST)
  * 힙은 상/하관계를 보장하며, BST는 좌/우 관계를 보장한다
  * 힙은 부모가 자식보다 작고, BST는 왼쪽 자식 < 부모 <= 오른쪽 자식 순이다.
  * 힙은 가장 작은/큰 값 추출 시 사용하고, BST는 모든 값에 대한 정렬이 필요한 경우 사용한다.
"""

class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    # For len(binaryheap)
    def __len__(self):
        return len(self.items) - 1

    """ 
    삽입 (Insert)
      * 힙에 요소를 삽입하기 위해서는 업힙 (Up-heap) 연산을 수행해야 함
      * 업힙 연산은 percolate_up() 함수로 정의함
      * 삽입하는 과정은 아래와 같음
        1. 요소를 가장 하위레벨의 최대한 왼쪽에 삽입 (배열의 마지막)
        2. 부모 값과 비교하여 값이 더 작은 경우 위치를 변경
        3. 적절한 곳까지 위치할 떄 까지 부모 노드와 비교 / 위치 변경을 반복
    """
    def _percolate_up(self):
        i = len(self)
        parent = i // 2

        while parent >= 0:
            if self.items[i] < self.itesm[parent]:
                self.itesm[parent], self.items[i] = self.items[i], self.itesm[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.itesm.append(k)
        self._percolate_up()


    """
    추출 (pop)
      * 추출 자체는 간편한편, root를 추출하면 됨 O(1)
      * 추출 이후, root의 빈자리를 채우면서 힙의 특성을 유지하는 작업 필요 O(log n)
      * 위와 같은 작업을 하는 함수를 percolate_down() 함수로 정의
      * 하강법 동작 방식은 아래와 같음
        1. 가장 마지막에 위치한 요소를 root 자리로 이동
        2. 해당 요소를 적절한 곳까지 위치할 떄 까지 자식 노드와 비교/위치 변경을 반복
    """

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx *  2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.itesm[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)


    def extract(self):
        extracted = self.items[1]
        self.itesm[1] = self.itesm[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted

