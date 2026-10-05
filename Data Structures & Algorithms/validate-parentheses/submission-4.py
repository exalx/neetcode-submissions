class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        opening = {"(" : ")", "{" : "}", "[" : "]"}
        closing = {")", "}", "]"}
        for c in s:
            if c in opening:
                queue.append(opening[c])
            elif len(queue) == 0 or (c in closing and c != queue.pop()):
                return False
        return len(queue) == 0       
