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
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        list_len: int = len(logs)
        dict_logs = {}
        
        for log in logs:
            key = log.split()[0]
            data = log.split()[0:]
            dict_logs[key] = data

        sorted(dict_logs.values())
        print(dict_logs)

        return []




if __name__=="__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    sol = Solution()
    print(sol.reorderLogFiles(logs))


