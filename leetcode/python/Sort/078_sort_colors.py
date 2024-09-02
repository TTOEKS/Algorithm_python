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

# My solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

# Book solution: Dutch national flag problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1


if __name__=="__main__":
    testcase = [2,0,2,1,1,0]
    print("hello world")

    sol = Solution()
    sol.sortColors(testcase)
    print(testcase)
