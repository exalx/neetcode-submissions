class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        order = sorted([v for v in count.values()], reverse=True)
        threshold = order[k - 1]
        result = []
        for n in count.keys():
            if count[n] >= threshold:
                result.append(n)
        return result

    