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
# My solution: Time exceeded
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            tmp = nums.copy()
            tmp.remove(num)
            res.append(math.prod(tmp))
        return res

# 자신을 제외한 값들을 좌우로 곱
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tmp = 1

        for i in range(len(nums)):
            res.append(tmp)
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]

        return res
"""


if __name__=="__main__":
	testcase = [1,2,3,4]
	print("hello world")

	sol = Solution()
	print(sol.productExceptSelf(testcase))
