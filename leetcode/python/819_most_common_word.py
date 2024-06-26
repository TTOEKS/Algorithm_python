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


## MY SOLUTINO (WIN)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        frequency = collections.defaultdict(int)
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        for word in words:
            frequency[word] += 1


        return max(frequency, key=lambda x:frequency[x])

"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
"""



if __name__=="__main__":
    arg = input()

    sol = Solution()
    print(sol.mostCommonWord(arg, ['hit']))

