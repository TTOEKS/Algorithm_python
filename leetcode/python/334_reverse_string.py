from typing import *


class Solution_my:
    def reverseString(self, s: List[str]) -> None:
        str_len:int = len(s)

        for i in range(str_len // 2):
            s[i], s[str_len - i - 1] = s[str_len -i - 1], s[i]

        """
        Do not return anything, modify s in-place instead.
        """
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

if __name__=="__main__":
    text = input()

    text_list = list(text)
    sol = Solution()
    sol.reverseString(text_list)

    print(text_list)
