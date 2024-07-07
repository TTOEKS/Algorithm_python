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
# my solution: 
class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)
"""

# solved by chaining using linked list
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict((ListNode))

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        cur = self.table[index]
        while cur:
            if cur.key == key:
                cur.value = value
                return
            if cur.next is None:
                break
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        cur = self.table[index]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        cur = self.table[index]
        if cur.key == key:
            self.table[index] = ListNode() if cur.next is None else cur.next
            return
        
        prev = cur
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev, cur = cur, cur.next


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
