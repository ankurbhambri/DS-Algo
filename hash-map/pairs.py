
# Idea: Use a hash map to count the occurrences of remainders when divided by 60, 24....any numbers.

# TC: O(n)
# SC: O(n)

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time):
        
        result = 0 
        mapping = {}

        for t in time:

            key = t % 60

            if key == 0:
                result += mapping.get(0, 0)
            else:
                result += mapping.get(60 - key, 0)

            mapping[key] = 1 + mapping.get(key, 0)
        
        return result


print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))  # Output: 3
print(Solution().numPairsDivisibleBy60([60,60,60]))  # Output: 3


# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/

class Solution:
    def countCompleteDayPairs(self, hours):

        result = 0 
        mapping = {}

        for h in hours:

            key = h % 24

            if key == 0:
                result += mapping.get(0, 0)
            else:
                result += mapping.get(24 - key, 0)

            mapping[key] = 1 + mapping.get(key, 0)
        
        return result

print(Solution().countCompleteDayPairs([12, 12, 12, 12, 12, 12]))  # Output: 15
print(Solution().countCompleteDayPairs([12, 12, 12, 12, 12, 6]))  # Output: 9
