class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxi = 0
        while l < r:
            if heights[l] < heights[r]:
                vol = heights[l] * (r - l)
                maxi = max(maxi, vol)
                l += 1
            else:
                vol = heights[r] * (r - l)
                maxi = max(maxi, vol)
                r -= 1
        return maxi