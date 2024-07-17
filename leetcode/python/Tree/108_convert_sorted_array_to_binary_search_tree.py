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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# MY SOLUTION: FAIL
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = len(nums) // 2
        left = start - 1
        right = start + 1

        def insert_tree(root, data):
            if root is None:
                root = TreeNode(data)
                return

            if root.val < data:
                insert_tree(root.left, data)
            else:
                insert_tree(root.right, data)

        root = TreeNode(nums[start])
        for idx in range(left, -1, -1):
            insert_tree(root.left, nums[idx])
        
        for idx in range(right, len(nums)):
            insert_tree(root.right, nums[idx])

        return root
        

# 계속해서 중간 것을 넣으면서 높이를 조절
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node


if __name__=="__main__":
	testcase = [-10, -3, 0, 5, 8]
	print("hello world")

	sol = Solution()
	print(sol.sortedArrayToBST(testcase))
