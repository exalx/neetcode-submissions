class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        etas = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        etas.sort(reverse=True)
        fleet = 1
        last_eta = etas[0][1]
        for i in range(1, n):
            n_eta = etas[i][1]
            if n_eta > last_eta:
                last_eta = n_eta
                fleet += 1
        return fleet
