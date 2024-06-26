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
My solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        tmp_str = ""
        digit_logs = []
        alpha_logs = []
        res = []
        
        for log in logs:
            tmp_str = "".join(log.split()[1:])

            if tmp_str.isdigit():
                digit_logs.append(log)

            if tmp_str.isalpha():
                alpha_logs.append(log)

        alpha_logs.sort(key=lambda x:x.split()[1:])

        return alpha_logs + digit_logs
"""

### WIN~!
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            if log.split()[1].isalpha():
                letters.append(log)

        letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))

        return letters + digits





if __name__=="__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    sol = Solution()
    print(sol.reorderLogFiles(logs))


