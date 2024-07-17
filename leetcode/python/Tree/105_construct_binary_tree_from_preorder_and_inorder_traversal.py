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
전위 순회의 첫번째값은 중위 순회 결과를 왼쪽/오른쪽 서브트리로 분할하는 역할을 함
"""
# Solved by Divided and conquer
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0 or len(inorder) <= 0:
            return

        index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])

        return node


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
