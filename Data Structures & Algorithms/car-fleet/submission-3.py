class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        etas = [[position[i], (target - position[i]) / speed[i]] for i in range(n)]
        etas.sort()
        fleet = 1
        last_eta = etas[-1][1]
        for i in range(n - 2, -1, -1):
            n_eta = etas[i][1]
            if n_eta > last_eta:
                last_eta = n_eta
                fleet += 1
        return fleet
