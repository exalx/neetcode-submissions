class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        starts = []
        for n in uniques:
            if n - 1 not in uniques:
                starts.append(n)
        
        if len(starts) == 1:
            return len(uniques)
        maxi = 0
        for s in starts:
            val = 1
            while s + 1 in uniques:
                val += 1
                s += 1
            if val > maxi:
                maxi = val
        return maxi
