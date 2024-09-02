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

class Solution:
    # do not use '+', '-' operator
    def getSum(self, a: int, b: int) -> int:
        # For binary translation (음수 처리)
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))

        if carry == 1:
            result.append('1')

        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK

        # 음수 처리
        if result > INT_MAX:
            result = ~(result ^ MASK)
        
        return result

if __name__=="__main__":
	print("hello world")

	sol = Solution()
	print(sol.getSum(-2, 3))
