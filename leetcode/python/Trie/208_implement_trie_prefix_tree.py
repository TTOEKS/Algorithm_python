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
# MY TRIE
# REFERENCE BY BOOK
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for chr in word:
            if chr not in node.children:
                newNode = TrieNode()
                node.children[chr] = newNode
            node = node.children[chr]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for chr in word:
            if chr not in node.children:
                return False
            node = node.children[chr]

        return node.word == True


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for chr in word:
            if chr not in node.children:
                return False
            node = node.children[chr]

        return True
"""

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def startWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in self.children:
                return False
            node = node.children[char]

        return True

if __name__=="__main__":
    testcase = []
    print("hello world")

    test = Trie()
    test.insert("test")

    node = test.root
    while len(node.children) >= 1:
        if node.word:
            break
        for ch in node.children:
            print(ch)
            node = node.children[ch]
