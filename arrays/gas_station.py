class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        difference = []

        for i in range(len(gas)):
            difference.append(gas[i] - cost[i])

        total = 0
        starting = 0
        for i in range(len(difference)):

            if total == 0:
                starting = i

            total += difference[i]

            if total < 0:
                total = 0

        return starting
