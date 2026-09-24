class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = -1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0 and zero < 0:
                zero = i
            elif n == 0:
                return [0 for i in range(len(nums))]
            else:
                product *= n
        
        if zero >= 0:
            products = [0 for i in range(len(nums))]
            products[zero] = product 
        else:
            products = []
            for i in range(len(nums)):
                products.append(product // nums[i])
        return products
