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
# My Solution: Use Counter of collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = collections.defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        res = sorted(count_dict.items(), key=lambda x: -x[1])[0]
        return res[0]

# Book solution: DP
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

# Book solution: Divided Conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

"""
# Book solution: python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]



if __name__=="__main__":
    testcase = [1,3,2,3,4,4,4]
    # testcase = [3,3,4]
    print("hello world")

    sol = Solution()
    print(sol.majorityElement(testcase))
