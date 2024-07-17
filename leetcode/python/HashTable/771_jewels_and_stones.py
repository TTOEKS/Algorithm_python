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
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for have in jewels:
            cnt += stones.count(have)
        return cnt

# Solve by dict (WIN)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        cnt = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for have in jewels:
            if have in freqs:
                cnt += freqs[have]
            
        return cnt

# Solved by defaultdict (WIN)
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        cnt = 0

        for char in stones:
            freqs[char] += 1
        
        for have in jewels:
            cnt += freqs[have]
            
        return cnt
        
# Solvec by counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        cnt = 0
        
        for have in jewels:
            cnt += freqs[have]
            
        return cnt


# Solved by pythonal
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
