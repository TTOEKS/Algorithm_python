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

"""""
# My solution : broute force (Time exceeded) O(n^2)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_height = max(height)

        for high in range(max_height):
            tmp_width = 0
            open_flag = False
            for i in range(len(height)):
                if height[i] > high:
                    if not open_flag:
                        open_flag = True
                    else:
                        res += tmp_width
                        tmp_width = 0
                else:
                    if open_flag:
                        tmp_width += 1
        return res
# Two pointer: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

"""
# Using Stack: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점 체크
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                # 이전 높이 차이 만큼 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)

        return volume




if __name__=="__main__":
    testcase = [0,1,0,2,1,0,1,3,2,1,2,1] 

    sol = Solution()
    print(sol.trap(testcase))
