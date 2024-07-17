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

# This is used sort function (not allow sort)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
"""

# By solution: solved by heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        res = 0
        
        for data in nums:
            heapq.heappush(hq, -data)


        for _ in range(k):
            res = heapq.heappop(hq)

        return -res


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)


        return heapq.heappop(nums)



if __name__=="__main__":
	testcase = [3,2,1,5,6,4]
	print("hello world")

	sol = Solution()
	print(sol.findKthLargest(
        testcase, 2))
