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


# 배열읍 입력 받아 합을 0으로 만드는 서로 다른 3개의 요소를 반환
# My Solution: Time Exceeded

"""
    Two Pointer 기법
    여러가지 방법이 존재하지만 대게 아래와 같이 동작
        1. 시작점(LEFT)과 끝점(RIGHT)를 설정
        2. 두 점을 이동하면서 문제를 수행
        * 범위를 좁히기 위해 정렬인 상태에서 유용함
        * Sliding window 방식과 유사함
        * ex) Binary Search 

"""
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        mid = 1

        while mid < length - 1:
            if mid > 1 and nums[mid] == nums[mid + 1]:
                mid += 1
                continue

            left = mid - 1
            right = mid + 1

            while left >= 0 and right < length:
                tmp_sum = nums[left] + nums[mid] + nums[right]
                print("{} {} {} / {}".format(nums[left], nums[mid], nums[right], tmp_sum))
                if tmp_sum < 0:
                    right += 1
                elif tmp_sum > 0:
                    left -= 1
                else:
                    if [nums[left], nums[mid], nums[right]] not in result:
                        result.append([nums[left], nums[mid], nums[right]])

                    while left > 0 and nums[left] == nums[left - 1]:
                        left -= 1

                    while right < length - 1 and nums[right] == nums[right + 1]:
                        right += 1
                    
                    if left >= 0:
                        left -= 1
                    if right < length:
                        right += 1

            mid += 1
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                print("{} {} {} / {}".format(i, left, right, sum))
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result

"""

if __name__=="__main__":
	testcase = [-2,0,1,1,2]
	print("hello world")

	sol = Solution()
	print(sol.threeSum(testcase))
