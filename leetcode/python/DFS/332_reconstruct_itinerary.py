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

"""
# My Soltuion: FAIL
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tmp_dict = {}

        if len(tickets) <= 1:
            return tickets

        for ticket in tickets:
            if ticket[0] in tmp_dict:
                tmp_dict[ticket[0]].append(ticket[1])
            else:
                tmp_dict[ticket[0]] = [ticket[1]]

        for item in tmp_dict.values():
            if len(item) > 1:
                item.sort()

        def dfs(start):
            stack = []
            path = []

            # print(tmp_dict)

            path.append(start)
            for idx in range(len(tmp_dict[start])):
                if tmp_dict[start][idx] in tmp_dict:
                    stack.append(tmp_dict[start][idx])
                    del(tmp_dict[start][idx])
                    break

            while stack:
                cur_visited = stack.pop()
                # print("CUR: {}".format(cur_visited))
                # print("INFO: ", tmp_dict[cur_visited])
                path.append(cur_visited)

                
                if cur_visited in tmp_dict and len(tmp_dict[cur_visited]) > 0:
                    for idx in range(len(tmp_dict[cur_visited])):
                        if tmp_dict[cur_visited][idx] in tmp_dict:
                            stack.append(tmp_dict[cur_visited][idx])
                            del(tmp_dict[cur_visited][idx])
                            break

            return path
        return dfs("JFK")
"""

# Solved by DFS (QUEUE)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        # {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)

        dfs('JFK')
        return route[::-1]


# Solved by DFS (Stack)
"""
Queue의 pop(0)은 O(n) 복잡도를 가지고 있음
Stack의 pop()은 O(1) 복잡도를 가지고 있음

그래서 이전 풀이에서 Queue를 Staack으로 최적화 하여 풀이

"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)
        dfs('JFK')
        return route[::-1]


# Solved by DFS iterative
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]





if __name__=="__main__":
    testcase = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]


    sol = Solution()
    print(sol.findItinerary(testcase))
