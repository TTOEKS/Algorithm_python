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
# My Solution: Broute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
# Using in struct
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            tmp_list = nums[:i] + nums[i+1:]
            expect = target - nums[i]
            if expect in tmp_list:
                return [i, nums.index(expect, i+1)]
        
        return []

"""
# Get key from result which minus first element
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i 

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

        return []



if __name__=="__main__":
    # testcase = [0,4,3,0]
    testcase = [2,7,11,15]

    sol = Solution()
    print(sol.twoSum(testcase, 9))
