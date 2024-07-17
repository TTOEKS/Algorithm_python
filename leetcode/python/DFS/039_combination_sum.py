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
# My Soltuion: I got a hint duplicated combination graph in Page 352
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start):
            candidates.sort()
            if sum(path) > target or len(path) >= 120:
                return
            if sum(path) == target:
                print("APPEND target in {}".format(start))
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(start)
                    start += 1
                    path.pop()
        dfs(0)
        return res
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return 
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        dfs(target, 0, [])
        return result




if __name__=="__main__":
	testcase = [8,2,6,3]

	print("hello world")

	sol = Solution()
	print(sol.combinationSum(testcase, 13))
