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
# My solution (FAIL)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur_array = []
        prev_array = []
        array = [i for i in range(1, n + 1)]
        visited = [False for _ in range(n)]
        result = []

        def dfs(elements):
            if len(elements) == (n - k):
                print(prev_array)
                result.append(prev_array[:])
                return

            for i in elements:
                cur_array = elements[:]
                cur_array.remove(i)

                prev_array.append(i)
                dfs(cur_array)
                prev_array.pop()

        dfs(array)
"""

"""
# Best Solved
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            if i > d: dfs(i-1)

            path.append(i)
            dfs(i-1)
            path.pop()
        dfs(n)
        return ans

"""

"""
# Solved by dfs
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        dfs([], 1, k)
        return result
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n + 1), k)

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol.combine(4, 2))
