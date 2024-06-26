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
문자열을 받아서 애너그램 단위로 그룹핑
풀이에 대해서 다시 고민해 볼것
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        result = []

        group = collections.defaultdict(list)

        for str in strs:
            ordered_str = "".join(sorted(str))
            group[ordered_str].append(str)

        for item in group.values():
            result.append(item)

        return result


if __name__=="__main__":
    testcase = ["eat","tea","tan","ate","nat","bat"]

    sol = Solution()
    print(sol.groupAnagrams(testcase))

