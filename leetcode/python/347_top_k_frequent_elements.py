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
# My solution: use Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)
        ordered_counter = counter.most_common(k)

        for ele in ordered_counter:
            res.append(ele[0])

        return res        
"""

# Solved by counter and heapq (WIN)
"""
해당 문제는 가장 큰 값을 관리하는 최대힙을 사용해야 함
파이썬은 heapq는 기본적으로 최소힙을 지원함
최대힙 사용을 위해서는 아래 2가지 방법을 사용해야 함
  - _heapify_max 와 같은 protected 멤버를 사용
  - 의도적으로 음수화 하여 저장해 가장 작은 값이 root에 위치하도록 함 (추천)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)
        counter_heap = []

        for f in counter:
            heapq.heappush(counter_heap, (-counter[f], f))

        print(counter_heap)

        for _ in range(k):
            res.append(heapq.heappop(counter_heap)[1])

        return res



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

if __name__=="__main__":
	testcase = [1,1,1,2,2,3] 
	print("hello world")

	sol = Solution()
	print(sol.topKFrequent(testcase, 2))
