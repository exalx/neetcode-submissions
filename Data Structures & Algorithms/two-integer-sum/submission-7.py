class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        n = len(nums)
        while nums[i] + nums[j] != target:
            if j == n - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        return [i, j]