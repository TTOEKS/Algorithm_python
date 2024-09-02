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
# My solution: FAIL
REASON: 하나의 UTF-8 단어에 대해서만 체크하는 것으로 착각함
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        num_char = 0

        first_byte = bin(data[0])[2:].zfill(8)
        print(first_byte)
        
        if len(data) == 1 and first_byte[0] != '0':
            return False

        for chr in first_byte:
            if chr == '1':
                num_char += 1
            else:
                break

        if num_char > 4:
            return False

        if num_char >= 2:
            num_char -= 1

        print(num_char)
        for num in data[1:]:
            ch_byte = bin(num)[2:].zfill(8)
            print(ch_byte)
            if ch_byte[0:2] == '10':
                num_char -= 1
            else:
                break

        return num_char == 0
"""
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False

        return True



if __name__=="__main__":
    # testcase = [197,130,1]
    # testcase = [10]
    # testcase = [240,162,138,147,145]
    testcase = [39,89,227,83,132,95,10,0]

    print("hello world")

    sol = Solution()
    print(sol.validUtf8(testcase))
