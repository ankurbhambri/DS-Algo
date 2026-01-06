# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, nums):

        total = sum(nums)
        if total % 2 != 0:
            return False  # Can't split an odd total into two equal parts

        target = total // 2

        # dp[i] means whether a subset sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: 0 sum is always possible (empty set)

        for num in nums:
            # Reverse loop taaki purani values overwrite na ho jayein
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

print(Solution().canPartition([1, 5, 11, 5]))  # Output: True
print(Solution().canPartition([1, 2, 3, 5]))   # Output: False

# Variant: What if numbers can be negative?

'''
Given an integer array nums, return true if you can partition the array into two subsets,
such that the sum of the elements in both subsets is equal or false otherwise. Numbers can be negative.

'''

def can_partition(nums):

    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    dp = {0}

    for num in nums:
        next_dp = set(dp)
        for s in dp:
            next_dp.add(s + num)
        dp = next_dp

    return target in dp

print(can_partition([1, 5, 11, 5])) # True
print(can_partition([1, 2, 3, 5]))  # False


# Follow-up 1: Return the two subsets if partition is possible

def solve():
    nums = [1, -2, 3, 2] # Example: Total sum = 4, Target = 2
    total = sum(nums)
    if total % 2 != 0: return False
    target = total // 2
    n = len(nums)
    
    memo = {}

    def backtrack(i, current_target):

        # Base Case
        if current_target == 0:
            return [] # Return empty list to signal success

        if i == n:
            return None
        
        state = (i, current_target)

        if state in memo:
            return memo[state]
        
        # 1. Include nums[i]
        res = backtrack(i + 1, current_target - nums[i])
        if res is not None:
            memo[state] = res + [nums[i]]
            return memo[state]
            
        # 2. Exclude nums[i]
        res = backtrack(i + 1, current_target)
        if res is not None:
            memo[state] = res
            return memo[state]
            
        memo[state] = None
        return None

    subset1 = backtrack(0, target)
    if subset1 is not None:
        # Subset 2 nikalne ke liye logic:
        # Original nums mein se subset1 ke elements hata do
        subset2 = nums.copy()
        for x in subset1:
            subset2.remove(x)
        return (subset1, subset2)
    return "Not Possible"

print(solve())


# Follow-up 2: return all the possible Partitions

def findAllPartitions(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return []
    
    target = total_sum // 2
    n = len(nums)
    all_subset1s = []
    
    def backtrack(start_index, current_subset, current_sum):
        # Base Case: Agar target mil gaya
        if current_sum == target:
            all_subset1s.append(list(current_subset))
            # Hum yahan return nahi karenge kyunki 0 ya negative numbers 
            # ki wajah se aage aur combinations mil sakte hain.
            if not any(x <= 0 for x in nums[start_index:]): 
                return # Optimization: Agar aage saare positive hain, toh ruk sakte hain

        if start_index == n:
            return

        for i in range(start_index, n):
            # 1. Include nums[i]
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset, current_sum + nums[i])
            
            # 2. Backtrack (Exclude nums[i])
            current_subset.pop()

    # Saare unique subset1 dhundne ke liye
    backtrack(0, [], 0)
    
    # Ab har subset1 ke liye uska counterpart subset2 nikalein
    final_result = []
    for s1 in all_subset1s:
        s2 = nums.copy()
        temp_s1 = s1.copy()
        # S2 nikalne ke liye S1 ke elements ek-ek karke remove karo
        for x in temp_s1:
            if x in s2:
                s2.remove(x)
        final_result.append((s1, s2))
        
    return final_result

# Example run:
nums = [1, 2, 3, 4, 2] # Total=12, Target=6
partitions = findAllPartitions(nums)
for i, (s1, s2) in enumerate(partitions):
    print(f"Partition {i+1}: Subset1={s1}, Subset2={s2}")