class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gas[i]-=cost[i]

        for i in reversed(range(len(gas)-1)):
            gas[i] += gas[i+1]

        if gas[0] < 0:
            return -1

        return gas.index(max(gas))