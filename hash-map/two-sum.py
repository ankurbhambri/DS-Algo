# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target: int):

        hm = {}

        for i, num in enumerate(nums):

            val = target - num

            if val in hm:

                return [hm[val], i] # return True, here if asked boolean

            hm[num] = i

        return []

print(Solution().twoSum([3, 3], 6))  # [0, 1]
print(Solution().twoSum([3, 2, 4], 6))  # [1, 2]
print(Solution().twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(Solution().twoSum([1, 2, 3, 4, 5], 10))  # []

# Variant: What if the problem was given in the context of dominoes, and you had to find the number of unique pairs that add up to some target?

def countUniqueDominoPairs(nums, target):

    seen = set()          # Jo numbers hum dekh chuke hain
    unique_pairs = set()  # Jo valid pairs humein mil chuke hain

    for num in nums:

        val = target - num
        
        if val in seen:
            # Pair ko hamesha sorted order mein rakhein (min, max)
            # Taki (4, 6) aur (6, 4) same treat hon
            pair = (min(num, val), max(num, val))
            unique_pairs.add(pair)
        
        seen.add(num)

    return len(unique_pairs), unique_pairs

print(countUniqueDominoPairs([1, 1, 2, 2, 3, 3], 4))  # (2, {(1, 3), (2, 2)})
print(countUniqueDominoPairs([1, 2, 3, 4, 5, 6], 7))  # (3, {(1, 6), (2, 5), (3, 4)})

# Similar questions

'''
    3Sum

    4Sum

    Two Sum II - Input Array Is Sorted

    Two Sum III - Data structure design

    Subarray Sum Equals K

    Two Sum IV - Input is a BST

    Two Sum Less Than K

    Max Number of K-Sum Pairs

    Count Good Meals

    Count Number of Pairs With Absolute Difference K

    Number of Pairs of Strings With Concatenation Equal to Target

    Find All K-Distant Indices in an Array

    First Letter to Appear Twice

    Number of Excellent Pairs

    Number of Arithmetic Triplets

    Node With Highest Edge Score

    Check Distances Between Same Letters

    Find Subarrays With Equal Sum

    Largest Positive Integer That Exists With Its Negative

    Number of Distinct Averages

    Count Pairs Whose Sum is Less than Target

'''