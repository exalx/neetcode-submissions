class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            if letters.get(l, None) is None:
                letters[l] = 1
            else:
                letters[l] += 1
        for l in t:
            if letters.get(l, None) is None:
                return False
            else:
                letters[l] -= 1
        for l, v in letters.items():
            if v != 0:
                return False
        return True 