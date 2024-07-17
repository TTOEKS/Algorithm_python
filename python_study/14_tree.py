"""
# 트리 (Tree)
계층형 트리 구조를 시뮬레이션 하는 추상 자료형 (ADT)로, Root와 parent-child 관계의 subtree로 구성되며, 서로 연결된 노드의 집합
  * 트리의 주요 특성: 재귀로 정의된 자기 참조 자료구조 (Recursively defined sefl-referential)
  * 여러 개의 서브트리들로 하나의 큰 트리를 구성

트리 자료구조의 주요 요소
  * Root: 모든 트리의 시작 지점 (최상단)
  * Child: Parent 노드의 바로 하위에 존재하는 노드
  * Edge: 노드들을 서로 연관시키는 간선
  * Height: 현재 위치에서부터 Leaf까지의 거리


Graph vs Tree
  * 트리는 순환 구조를 갖지 않는 그래프이다.
  * 트리는 그래프의 범주에 속하지만 아래와 같은 구분점이 있음 
    * 트리는 순환 구조를 가질 수 없음 (Cyclic)
    * 하나의 부모 노드만 가짐
    * 방향은 부모노드에서 자식 노드로 단방향
    * 모든 노드가 최소 하나 이상의 간선으로 연결

Binary Tree
  * 트리 중 가장 널리 사용되는 트리 자료구조는 Binary Tree와 Binary Search Tree 이다.
  * 각 노드가 m개 이하의 자식을 가진 경우 m-ary tree라고 함
  * m-ary tree에서 m = 2 인 경우를 Binary Tree라고 함

Binary Tree의 유형
  * 정 이진 트리 (Full Binary Tree): 모든 노드가 0개 또는 2개의 자식 노드를 가짐
  * 완전 이진 트리 (Complete Binary Tree): 마지막 레벨을 제외한 모든 레벨이 완전히 채워져 있고, 마지막 레벨은 왼쪽부터 자식이 채워짐
  * 포화 이진 트리 (Perfect Binary Tree): 모든 노드가 2개의 자식 노드를 가지고 있음

직렬화 역직렬화
'이진 트리' 데이터는 논리적인 구조이다. 
  * 파일 혹은 디스크에 저장하기 위해서는 물리적인 형태로 변환해주어야 함 (직렬화 / 역직렬화)
  * 트리 구조를 배열이나 리스트과 같은 선형 자료구조로 변환하는 과정
  * 이진트리를 배열로 표현하면 부모-자식 간의 관계를 index로 알 수 있다는 장점이 존재함 
    * node n -> 부모 노드: n / 2 | 왼쪽 자식 노드: 2n | 오른쪽 자식 노드: 2n + 1
    * 비어있는 노드는 NULL 로 표현할 수 있음
  * BFS, DFS 모두 가능하지만, 직관적으로 BFS가 더 뛰어남 (순서대로 배치됨)

이진 탐색 트리 (BST: Binary Search Tree)
  * 자식 노드가 2개 이하이면서 정렬되어 있는 트리이다.
  * 왼쪽 서브트리는 작은값 / 오른쪽 서비트리는 같거나 큰 값
  * 크기에 따라 왼쪽, 오른쪽으로 정렬이 되어 있는 트리로 탐색 시간 복잡도는 O(log n)
  * 이진 탐색 트리는 트리의 균형이 시간 복잡도를 결정하며, O(log n) ~ O(n)이다
  * 균형이 나쁜 트리는 성능이 나쁘기 때문에 스스로 균형을 맞추는 '자가 균형 이진 트리'가 등장

자가 균형 이진 탐색 트리 (Self-Balanced Binary Search Tree)
  * 최악의 경우에도 이진 트리의 균형이 잘 맞도록 유지함
  * Height를 최대한 낮게 유지하는 것이 포인트이다.
  * 대표적으로 AVL Tree, red-balck Tree가 있음
  * 실무에서는 Red-Black Tree를 ㅂ자주 사용함
  * JAVA의 Hashmap은 테이블의 Chainging 시, LinkedList와 함께 Red-Black Tree를 병행 사용
"""

"""
Tree traversal (트리 순회)
그래프 순회의 한 형태로 트리 자료구조에섯 각 노드를 정확히 한번 방문하는 과정
  * 그래프 순회와 마찬가지로, BFS, DFS로 탐색을 수행함
  * DFS 순회의 경우 방문 순서에 따라 아래 3가지 방식으로 구분
    1. 전위 순회 (Pre-order, NLR)
    2. 중위 순회 (In-Order, LNR)
    3. 후위 순회 (Post-Order, LRN)
    * L: 현재 노드의 왼쪽 서브트리, N: 현재 노드, R: 현재 노드의 오른쪽 서브트리
  * 3가지 순회 중 2가지 결과만 있어도 원래 트리를 원복할 수 있음

"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)

def postorder(node):
    if node is None:
        return 

    postorder(node.left)
    postorder(node.right)
    print(node.val)


if __name__=="__main__":
    pass

