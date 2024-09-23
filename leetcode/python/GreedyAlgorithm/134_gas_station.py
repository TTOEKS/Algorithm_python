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
# My solutino: Time exceed
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_info = {}
        gas_capacity = 0
        res = -1

        # 이거 넣고 성공
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            gas_info[i] = (gas[i], cost[i])
        least_cost_gas_info = dict(sorted(gas_info.items(), key=lambda x: (x[1][1], -x[1][0])))

        for start in least_cost_gas_info.keys():
            res = start
            gas_capacity = 0
            for idx in range(len(gas)):
                infos = gas_info[(idx + start) % len(gas)]

                if gas_capacity < 0:
                    break

                gas_capacity += infos[0]
                gas_capacity -= infos[1]
            if gas_capacity >= 0:
                break

        return res if gas_capacity >= 0 else -1
"""

# BOOK SOLUTION: Traveraal all -> Time exceed
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 넣어도 실패
        if sum(gas) < sum(cost):
            return -1

        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_traversal = True
                if gas[index] + fuel < cost[index]:
                    can_traversal = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_traversal:
                return start
        return -1



# BOOK SOLUTION: Traveraal once
"""
다 돌지 않고, 모두 방문이 가능한지 확인만
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start


if __name__=="__main__":
    """
    testcase1 = [1,2,3,4,5]
    testcase2 = [3,4,5,1,2]

    testcase1 = [5,1,2,3,4]
    testcase2 = [4,4,1,5,1]
    """

    testcase1 = [5,8,2,8]
    testcase2 = [6,5,6,6]

    print("hello world")

    sol = Solution()
    print(sol.canCompleteCircuit(testcase1, testcase2))


