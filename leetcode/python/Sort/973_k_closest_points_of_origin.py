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
# My solution
class Solution:
    @staticmethod
    def calc_distance_from_origin(x):
        return math.sqrt(x[0] ** 2 + x[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp = {}
        for i in range(len(points)):
            tmp[i] = self.calc_distance_from_origin(points[i])

        # 람다 함수 참고
        sorted_keys = sorted(tmp, key=lambda x: tmp[x])
        result = list(map(lambda x: points[x], sorted_keys[:k])) 

        return result
"""

# Book solution: eclidean distance and prirority queue (WIN)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        print(heap)

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result


        


if __name__=="__main__":
	testcase = [[3,3],[5,-1],[-2,4]]
	print("hello world")

	sol = Solution()
	print(sol.kClosest(testcase, 2))
