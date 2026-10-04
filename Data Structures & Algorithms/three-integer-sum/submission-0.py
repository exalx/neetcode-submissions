class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        uniques = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a, b = nums[i], nums[j]
                c = - (a + b)
                if c in uniques and uniques[c] not in (i, j):
                    t = sorted([a, b, c])
                    rep = f"{t[0]},{t[1],}{t[2]}"
                    if rep not in seen:
                        result.append(t)
                        seen.add(rep)
        return result
