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

# Solved by dijkstra algorithm used pirority queue (min heap)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w, in times:
            graph[u].append((v, w))

        # 큐 변수 [(time, node)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            print(dict(graph))
            print(dict(dist))
            print()
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w, in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        print()

        if len(dist) == n:
            return max(dist.values())

        return -1


"""
# Best Solved
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x : [] for x in range(1, n + 1)}

        for source, dest, time in times:
            adj[source].append((dest, time))

        visited = set()
        costs = {x: math.inf for x in range(1, n + 1)}
        costs[k] = 0
        queue = [(0, k)]
        res = 0 

        while queue:
            time, node = heappop(queue)

            if node in visited: 
                continue
            
            res = max(res, time)
            visited.add(node)

            for dest, time in adj[node]:
                if costs[dest] > costs[node] + time:
                    costs[dest] = costs[node] + time
                    heappush(queue, (costs[dest], dest))

        return res if len(visited) == n else -1
"""


if __name__=="__main__":
	testcase = [[2,1,1],[2,3,1],[3,4,1]]
	print("hello world")

	sol = Solution()
	print(sol.networkDelayTime(testcase, 4, 2))
