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
# My solution: greedy with priority queue 
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []
        res = []

        for data in people:
            heapq.heappush(hq, (-data[0], data))

        for _ in range(len(hq)):
            person = heapq.heappop(hq)[1]
            index = 0
            cnt = person[1]

            for data in res:
                if cnt <= 0:
                    break

                if person[0] <= data[0]:
                    cnt -= 1
                    index += 1
            res.insert(index, person)

        return res
            

# Solved by book (prioirty queue, greedy)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
"""
# Solved by sort
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        output = []
        print(people)
        for p in people:
            output.insert(p[1],p)
        return output

if __name__=="__main__":
    testcase = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print("hello world")

    sol = Solution()
    print(sol.reconstructQueue(testcase))
