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

# Book solution: recusrive broute force  (FAIL: Time exceeded)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i: int) -> int:
            if i < 0:
                return 0
            return max(helper(i - 1), helper(i - 2) + nums[i])
        return helper(len(nums) - 1)

# Book solution: Tabluation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        print(dp)
        print()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        print(dp)
        print()

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            print(dp)
            print()

        return dp.popitem()[1]





if __name__=="__main__":
    testcase = [2,7,9,3,1]
    print("hello world")

    print("testcase: ", testcase)
    sol = Solution()
    print(sol.rob(testcase))
