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

# DFS의 플로우를 고민한 후, 각 인자를 적절하게 처리해야 함 (여기서는 start를 제대로 사용 못함)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(start, path):
            result.append(path)
            
            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result


if __name__=="__main__":
	testcase = [1, 2, 3]
	print("hello world")

	sol = Solution()
	print(sol.subsets(testcase))
