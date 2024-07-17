"""
패린드롬 (Palindrome, 회문)
앞 뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어

ex) 소주 만병만 주소 -> 소주 만 병만 주소
ex) 기러기 -> 기러기
"""

import collections
import re

class Solution_my:
    def isPalindrome(self, s: str) -> bool:
        str_list:list = []
        str_len: int
        for ch in s:
            if ch.isalnum():
                str_list.append(ch.lower())

        str_len = len(str_list)
        for i in range(str_len//2):
            if str_list[i] != str_list[str_len - i - 1]:
                return False
        return True

""" 
List pop
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list:list = []
        for ch in s:
            if ch.isalnum():
                str_list.append(ch.lower())

        while len(str_list) > 1:
            if str_list.pop(0) != str_list.pop():
                return False
        return True
Deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: collections.deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

"""
Regex & slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


if __name__=="__main__":
    text = input("")

    solution = Solution()
    print(solution.isPalindrome(text))
