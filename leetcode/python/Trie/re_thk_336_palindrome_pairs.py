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

# Solved by BF (Time limited excced)
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def check_possible(word1, word2):
            set_word1 = set(word1)
            set_word2 = set(word2)
            if set_word1.issubset(set_word2):
                return True

            if set_word2.issubset(set_word1):
                return True

            return False

        def check_palindrome(word):
            left = 0
            right = len(word) - 1

            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1

            return True

        res = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if check_possible(words[i], words[j]):
                    if check_palindrome(words[i] + words[j]):
                        res.append([i, j])

                    if check_palindrome(words[j] + words[i]):
                        res.append([j, i])

        return res

# Solved by Trie (so hard...)
class TrieNode:
    def __init__(self):
        self.palindrome_word_ids = []
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]


    # 애초에 삽입시, 뒤집어서 삽입
    def insert(self, index: int, word: str):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)

            node = node.children[char]
        node.word_id = index

    def search(self, index, word):
        node = self.root
        result = []

        while word:
            # Check Logic #3
            # 탐색 중간에 word_id가 있고, 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]


        # Check logic #1
        # 끝까지 탐새 했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])


        # Check logic #2
        # 끝까지 탐색 했을 때 Palindrome_word_ids가 있는 경우
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word, in enumerate(words):
            results.extend(trie.search(i, word))

        return results

"""

# Best Solution
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        print(backward)
        for i, word in enumerate(words):
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
                
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res



if __name__=="__main__":
    # testcase = ["abcd","dcba","lls","s","sssll"]
    # testcase = ["a",""]
    testcase = ["abcd","dcba","lls","s","sssll"]
    print("hello world")

    sol = Solution()
    print(sol.palindromePairs(testcase))
