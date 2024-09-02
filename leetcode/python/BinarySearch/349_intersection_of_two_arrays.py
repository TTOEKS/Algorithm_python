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
    def binary_search(self, nums, target):
        length = len(nums)
        if length == 1 and nums[0] != target:
            return False

        mid = length // 2
        if nums[mid] > target:
            return self.binary_search(nums[:mid], target)
        elif nums[mid] < target:
            return self.binary_search(nums[mid:], target)
        else:
            return True
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] 
        nums1.sort()
        nums2.sort()

        if len(nums1) < len(nums2):
            for num in nums1:
                if num not in res:
                    if self.binary_search(nums2, num):
                        res.append(num)
        else:
            for num in nums2:
                if num not in res:
                    if self.binary_search(nums1, num):
                        res.append(num)
    
        return res

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniq_num1 = []
        uniq_num2 = []
        res = [] 

        for num in nums1:
            if num not in uniq_num1:
                uniq_num1.append(num)
        uniq_num1.sort()

        for num in nums2:
            if num not in uniq_num2:
                uniq_num2.append(num)
        uniq_num2.sort()
        
        if len(uniq_num1) < len(uniq_num2):
            for num in uniq_num1:
                if num in uniq_num2:
                    res.append(num)
        else:
            for num in uniq_num2:
                if num in uniq_num1:
                    res.append(num)

        return res
"""



# Solved by bisearch (WIN)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result

# Solved by two points
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums1.sort()
        nums2.sort()

        i = j = 0
        while i < len(nums1)  and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result


if __name__=="__main__":
	testcase1 = [4,9,5]
	testcase2 = [9,4,9,8,4]
	print("hello world")

	sol = Solution()
	print(sol.intersection(testcase1, testcase2))
