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
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # My Dfs (FAIL)
        def dfs(start, path):
            if len(path) == len(nums) or start >= len(nums):
                print(path)
                path.clear()
                return
            print("start: {} / path: {} / expected: {}".format(start, path, nums[start]))
            path.append(nums[start])

            for i in range(0, len(nums)):
                if i != start and nums[i] not in path:
                    path.append(nums[i])
                    dfs(start + 1, path)
                    # print("END DFS at {}, {}".format(i, j))
        dfs(0, [])
"""


"""
# Solved by dfs
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
        def dfs(elements):
            if len(elements) == 0:
                # Not result.append(prev_elements) <- This append prev_elements referece so, can change elements
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()


        dfs(nums)
        return result
"""
"""
# BEST SOLUSION
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(array, used):
            if len(array) == len(nums):
                output.append(array.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    array.append(nums[i])
                    used[i] = True
                    dfs(array, used)
                    array.pop()
                    used[i] = False
        dfs([], [False] * len(nums))
        return output
"""

# Solved by itertools
"""
itertools
반복자 생성에 최적화된 효율적인 기능 제공
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


if __name__=="__main__":
    testcase = [1,2,3]
    print("hello world")

    sol = Solution()
    print(sol.permute(testcase))
