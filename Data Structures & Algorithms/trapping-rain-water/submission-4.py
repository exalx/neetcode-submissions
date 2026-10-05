class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        l, r = 0, len(height) - 1
        lvl = 0
        while l < r:
           while height[l] < height[r]:
            if height[l] < lvl:
                vol += lvl - height[l]
            else:
                lvl = height[l]
            l += 1
           lvl = height[r]
           while height[r] < height[l]:
            if height[r] < lvl:
                vol += lvl - height[r]
            else:
                lvl = height[r]
            r -= 1
           lvl = height[l]
           if height[l] == height[r]:
            l += 1
        return vol
