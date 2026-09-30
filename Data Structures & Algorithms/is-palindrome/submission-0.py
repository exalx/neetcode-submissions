class Solution:
    def isPalindrome(self, s: str) -> bool:
        short = []
        for l in s:
            if l.isalnum() :
                short.append(l.lower())
        print(short)
        left = 0
        right = len(short) - 1
        while left < right:
            if short[left] != short[right]:
                return False
            left += 1
            right -= 1
        return True