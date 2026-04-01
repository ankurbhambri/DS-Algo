# https://leetcode.com/problems/robot-collisions/

from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):

        res = []
        stack = deque()
        n = len(positions)
        indices = list(range(n))

        # Sort indices based on their positions
        indices.sort(key=lambda x: positions[x])

        for current_index in indices:

            # Add right-moving robots to the stack
            if directions[current_index] == "R":
                stack.append(current_index)

            else:
                while stack and healths[current_index] > 0:

                    # Pop the top robot from the stack for collision check
                    top_index = stack.pop()

                    if healths[top_index] > healths[current_index]:
                        # Top robot survives, current robot is destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)

                    elif healths[top_index] < healths[current_index]:
                        # Current robot survives, top robot is destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0

                    else:
                        # Both robots are destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

        # Collect surviving robots
        for index in range(n):
            if healths[index] > 0:
                res.append(healths[index])

        return res


print(Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], ["R", "R", "L", "L"])) # Output: [14]
print(Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], ["R", "L", "R", "L", "R"])) # Output: [2, 3, 2]