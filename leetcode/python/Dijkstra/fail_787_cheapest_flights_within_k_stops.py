import collections
import heapq
import functools
import sys
import math
import bisect
import pprint
from typing import *

"""
# My Solution : FAIL
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = collections.defaultdict(list)

        for u, v, w in flights:
            flight_dict[u].append([v, w])

        minheap = [(src, 0)]
        distance = [-1 for _ in range(len(flights))]

        for _ in range(k):
            if not minheap:
                break
            cur, weight = heapq.heappop(minheap)
            if distance[cur] == -1:
                distance[cur] = weight
                for v, w in flight_dict[cur]:
                    heapq.heappush(minheap, (v, weight + w))

        for v, w in minheap:
            if distance[v] == -1 or (distance[v] > w):
                distance[v] = w

        return distance[dst]

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {x: [] for x in range(n)}

        for source, destination, weight in flights:
            adj[source].append((destination, weight))

        visited = set()
        distances = {x: math.inf for x in range(n)}
        distances[src] = 0
        queue = [(0, src, k)]


        while queue:
            weight, node, rest = heapq.heappop(queue)

            if node == dst:
                return weight

            if rest < 0:
                break

            if node in visited:
                continue

            visited.add(node)

            for v, w in adj[node]:
                if distances[v] > distances[node] + w:
                    distances[v] = distances[node] + w
                    heapq.heappush(queue, (distances[v], v, rest - 1))

        return distances[dst] if distances[dst] != math.inf else -1

"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w, in flights:
            graph[u].append((v, w))

        Q = [(0, src, k)]

        while Q:
            price, node, rest = heapq.heappop(Q)
            if node == dst:
                return price

            if k >= 0:
                for v, w, in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, rest - 1))

        return -1






if __name__=="__main__":
    # FAIL CASE
    testcase = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]

    print("hello world")

    sol = Solution()
    # FAIL CASE 
    print(sol.findCheapestPrice(4, testcase, 0, 3, 1))
