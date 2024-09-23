# 다이나믹 프로그래밍 (DP: Dynamic Programming)
"""
각각의 작은 문제로 나누어 해결한 결과를 저장한 후, 나중에 큰 문제의 결과와 합하여 풀이
  * 응용 수학자 리차드 벨만이 고안한 알고리즘 (아래는 벨만이 고안한 다양한 이론)
    - Bellman-Ford 알고리즘
    - Machine Learning 분야의 차원의 저주 (Curse of Dimensionality)
  * 최적 해결 방법이 부분 문제에 대한 최적 해결 방ㅂ업으로 구성되는 문제에서 활용
    - 최적 부분 구조 (Optimal Substructure)
  * Greedy Algorithm과 차이 (Greedy / DP)
    - 항상 현재 시점의 최적에 접근 / 중복된 하위 문제 결과를 저장 후 풀이
  
알고리즘과 풀이 가능한 문제들 특징
알고리즘 | 풀이 가능한 문제 특징            | 풀이 가능한 문제 및 알고리즘
------------------------------------------------------------------------------------
DP       | 최적 부분 구조, 중복된 하위 문제 | 0-1 배낭, 파보나치 수열, 다익스트라
------------------------------------------------------------------------------------
Greedy   | 최적 부분 구조, 탐욕 선택 속성   | 분할 가능 배낭 문제, 다익스트라
------------------------------------------------------------------------------------
분할 정복| 최적 부분 구조                   | 병합 정렬, 퀵 정렬
------------------------------------------------------------------------------------

다이나믹 프로그래밍 방법론
  * 방식에 따라 상향식 (Bottom-up: Tabulation), 하양식 (Top-down: Memoization)으로 구분 가능
  * 상향식
    더 작은 하위 문제부터 살핀 후, 작은 문제의 정답을 이용해 큰 문제를 해결
    (일반적으로 다이나믹 프로그램을 지칭하는 방식)
  * 하양식
    하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 자연스러운 방식으로 해결

대부분의 다이나믹 프로그래밍 문제는 어려운 편에 속하기 때문에 다양한 문제를 인터뷰에서 출제하기 어려움
관련 문제를 출제하더라도 기본에 가장 충실한 문제를 출제할 가능성이 높음 (기본: 파보나치 수열)
파보나치 수열은 재귀와 다이나믹 프로그래밍을 평가할 수 있는 좋은 기본 문제임
"""

from typing_extensions import NoDefault



# 파보나치 수열
# 재귀 브루트 포스
def fib(n):
    if n <= 1:
        return None
    return fib(n - 1) + fib(n - 2)

class Solution:
    dp = collections.defaultdict(int)
    # 하양식
    def fib(self, n):
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = fib(n - 1) + fib(n - 2)
        return self.dp[n]

    # 상향식
    def fib(self, n):
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]


# 0-1 배낭 문제
"""
다이나믹 프로그래밍의 대표적인 문제라고 할 수 있음
이전의 Greedy와 유사하지만, 짐을 쪼갤 수 없다는 점이 다름
"""

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]
def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])

    return pack[-1][]







