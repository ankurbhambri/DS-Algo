# https://leetcode.com/problems/gas-station/description/


# TC: O(n)
# SC: O(1)

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
          
            if total_tank < 0:
                starting_station = i + 1
                total_tank = 0

        return starting_station if starting_station < len(gas) else -1

print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
print(Solution().canCompleteCircuit([2,3,4], [3,4,3]))  # Output: -1
print(Solution().canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))  # Output: 4
print(Solution().canCompleteCircuit([1,2,3,4,5], [2,3,4,5,1]))  # Output: 4



# Brute Force Approach
# TC: O(n^2)
# SC: O(1)

def canCompleteCircuit(gas, cost):
    n = len(gas)
    
    for start in range(n):
        tank = 0
        completed = True
        for i in range(n):
            idx = (start + i) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                completed = False
                break
        if completed:
            return start
    return -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
print(canCompleteCircuit([2,3,4], [3,4,3]))  # Output: -1
print(canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))  # Output: 4
print(canCompleteCircuit([1,2,3,4,5], [2,3,4,5,1]))  # Output: 4
