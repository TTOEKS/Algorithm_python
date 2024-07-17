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

# My solution (solved by bfs)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque()

        def bfs(node: TreeNode):
            queue.append(node)

            while queue:
                tmpNode = queue.popleft()
                if tmpNode:
                    tmpNode.left, tmpNode.right = tmpNode.right, tmpNode.left
    
                    if tmpNode.left is not None:
                        queue.append(tmpNode.left)
    
                    if tmpNode.right is not None:
                        queue.append(tmpNode.right)
        bfs(root)
        return root


# Solved by recursive
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        # right = left = None
        # if root.left:
        left = self.invertTree(root.left)
        # if root.right:
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
    
        return root


# Solved by dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        return root

# Solve dby post-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left
        return root






if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
