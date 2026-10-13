class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        queue = []
        s = 0
        for h in heights:
            l = 0
            while queue and queue[-1] > h:
                l += 1
                s = max(s, queue.pop() * l)
            for i in range(l + 1):
                queue.append(h)
        l = 0
        while queue:
            l += 1
            s = max(s, queue.pop() * l)
        return s
            