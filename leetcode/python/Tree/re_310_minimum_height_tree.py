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

# My Solution: FAIL: BFS로 하였으나, height 게산을 제대로 못함
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        res = []
        min_height = math.inf

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(start):
            change_flag = False
            visited = [False for _ in range(n)]
            queue = collections.deque()
            queue.append(start)
            visited[start] = True
            height = -1

            while queue:
                cur = queue.popleft()
                for next in graph[cur]:
                    if visited[next] == False:
                        if not change_flag:
                            height += 1
                            change_flag = True
                        visited[next] = True
                        queue.append(next)
                if change_flag:
                    change_flag = False
            return height


        for start in range(n):
            height = bfs(start)
            print("START: {} / HEIGHT: {}".format(start, height))
            if height < min_height:
                res.clear()
                min_height = height
            if height == min_height:
                res.append(start)
        return res


# Solved by remove leaf
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫번째 리프노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 리프 노드를 하나씩 없애면서 반복
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves



if __name__=="__main__":
    # testcase = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    testcase = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    print("hello world")

    sol = Solution()
    print(sol.findMinHeightTrees(6, testcase))
