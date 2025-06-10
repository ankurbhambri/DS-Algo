# https://leetcode.com/problems/brick-wall/

# Idea, we can use a hash map to count the number of gaps at each position.
# The key will be the position of the gap, and the value will be the count of how many rows have a gap at that position.

class Solution:
    def leastBricks(self, wall):

        gaps = {0: 0}

        # counts gaps first
        for line in wall:

            prev = 0

            for brick in line[:-1]:

                prev += brick

                gaps[prev] = 1 + gaps.get(prev, 0)

        # then number of rows - max(gaps) value
        return len(wall) - max(gaps.values())


print(Solution().leastBricks([[1],[1],[1]]))  # Output: 3
print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))  # Output: 2
