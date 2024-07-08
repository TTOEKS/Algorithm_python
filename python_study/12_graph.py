"""
비선형 자료구조 (그래프)
  * 선형 자료구조와 달리 Multi-level로 자료가 구성됨
  * 탐색이 복잡하고 구현이 어려움
  * 메모리르 좀 더 효율저긍로 사용 가능
  * 대표적: 그래프 자료구조
  * 탐색: Dijkstra, Shortest-path problem
"""
"""
그래프 자료구조
그래프 이론에서 그래프는 객체 일부 쌍(Pair)가 연관되어 있는 객체 집합 구조를 뜻한다.

오일러 경로
  * 그래프 이론이 발생하기된 시초 이론
  * 정점 (VERTEX), 간선(EDGE), 차수(DEGREE) 개념 정립
  * 모든 정점이 짝수개의 차수를 가진다면, 모든 간선을 거처 목적지에 도착 가능
  * 모든 간선을 한번 씩 방문하는 유한그래프 (Fitnite Graph)

해밀턴 경로: 각 정점을 한번씩 방문하는 무향 또는 유향 그래프
  * 오일러 경로와 다른 점: 오일러 경로 -> 간선 기준 / 해밀턴 경로 -> 정점 기준
  * 최적 알고리즘이 없는 대표적인 NP-Complete 문제
  * 원래 출발점으로 돌아오는 경로는 해밀턴 순환이라 함
  * 특히, 최단 거리를 찾는 문제는 외판원 문제로 유명함 (TSP)

외판원 문제 (Travelling Salesman Probelm)
여러 도시가 존재하는 나라에서 각 도시를 한번 씩 방문했을 때, 어떤 순서로 방문해야 짧은 거리로 방문 가능한가?
  * 20개의 도시가 존재할 때 : 20! (240 경 번의 경우의 수가 있음)
  * Dynamic Prgramming 기법을 사용하면 O(n^2 * 2^n) 번으로 줄일 수 있음
  * Brute Force : 240경 번 -> Dynamic Programming: 419,430,400 번

정리
  * 해밀턴 경로: 한번만 방문하는 경로
  * 해밀턴 순환: 한번만 방문해서 출발지로 돌아오는 경로
  * 외판원 문제: 한번만 방문해서 출발지로 돌아오는 경로 중 최단 거리
"""
"""
NP 복잡도
NP는 비결정론적 튜링 기계 (NTM)로 다항시간 안에 풀수 있는 판정 문제의 집합 
  * NP에 속하는 문제들은 결정론적 튜링 기계로 다항시간에 검증 가능하고 역도 가능
  * 결정론적 튜링 기계로 다항시간 안에 풀 수 있는문제는 비결정론적 튜링 기계로도 다항시간 안에 풀 수 있음
  * 즉, P 집합은 NP 집합의 부분집합 -> P가 NP의 진부분집합인지 P와 NP가 같은지 난제
  * 위와 같은 난제를 P-NP 난제라고 현재까지 풀리지 않은 문제임
"""

""" 
그래프 순회
그래프 탐색이라고도 불리며, 그래프의 각 정점을 방문하는 과정을 의미한다.
  * 그래프의 각 정점을 방문하는 Traverlling에는 아래 2가지 알고리즘이 존재함
    * 깊이 우선 탐색 (DFS: Depth-First Search)
      * 스택이나 재귀로 구현 (재귀가 더 간단하게 구현 가능)
      * BackTracking 에서 좋은 성능을 보임
    * 너비 우선 탐색 (BFS: Breadth-First Search)
      * 큐로 구현
      * 일반적으로 자주 사용되는 알고리즘

  * 그래프 표현 방법
    * 인접 행렬 (Adjacency Matrix)
    * 인접 리스트 (Adjacnecy List)
"""

"""
백 트래킹 (backTracking)
해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(Backtrack)해 정답을 찾아감
  * 범용적인 알고리즘 중 하나로 제약 충족 문제 (Constraint Satifaction problem)에 유용
  * 즉, 탐색하다 더 갈 수 없으면 왔던 길을 되돌아가 다른 길을 찾는 것
  * 백 트래킹은 주로 재귀함수로 구현
  * 알고리즘마다 DFS 변형이 있지만, 모두 DFS 범주에 속함
  * 최악의 경우 모든 경우의 수를 봐야한다는 단점이 있음
  * 탐색 중 가능성이 없는 경우 포기한다는 점에서 더 효율적임

제약 충족 문제 (Constraint Satisfaction Problems, CSP)
수 많은 제약을 충족하는 상태를 찾아내는 수학적인 문제를 일컫는다.
  * 인공지능, 경영과학 분야에서 심도 있게 연구가 진행 되고 있음
  * 대표적인 제약 충족 문제는: 스도쿠가 있음
  * 이러한 다양한 제약 조건을 충족하기 위해 가지치기를 통해 최적화 하는 것이 좋음
  * 백 트래킹 기법이 유용하게 사용되는 경우도 이러한 경우 
"""

def recursive_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        discovered = recursive_dfs(w, discovered)
    return discovered

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered

if __name__=="__main__":
    print("Hello world")




