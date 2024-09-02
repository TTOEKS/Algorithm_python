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

class Solution:
    @staticmethod
    def check_swap(a: int, b: int):
        return str(a) + str(b) < str(b) + str(a)

    def largestNumber(self, nums: List[int]) -> str:
        pivot = 1

        while pivot < len(nums):
            cur = pivot
            while cur > 0 and self.check_swap(nums[cur - 1], nums[cur]):
                nums[cur], nums[cur - 1] = nums[cur - 1], nums[cur]
                cur -= 1
            pivot += 1

        return str(int("".join(map(str, nums))))


# best solution
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(0, len(nums)):
            nums[i] = str(nums[i])
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int(''.join(nums)))

if __name__=="__main__":
	testcase = [3,30,34,5,9]
	print("hello world")

	sol = Solution()
	print(sol.largestNumber(testcase))
