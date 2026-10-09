class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        warmer = [0] * n
        queue = [0]
        for i in range(1, n):
            t = temperatures[i]
            while len(queue) > 0 and t > temperatures[queue[-1]]:
                j = queue.pop()
                warmer[j] += i - j
            queue.append(i)
        return warmer
