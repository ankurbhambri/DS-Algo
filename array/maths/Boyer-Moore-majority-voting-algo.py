def majority_element(nums):
    # Phase 1: Find a candidate
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num  # Set new candidate
        count += (1 if num == candidate else -1)
    
    # Phase 2: Verify if the candidate is actually the majority element
    candidate_count = 0
    for num in nums:
        if num == candidate:
            candidate_count += 1

    # Check if the candidate appears more than n/2 times
    if candidate_count > len(nums) // 2:
        return candidate_count, candidate

    return -1, -1

# Example usage
nums = [3, 2, 3]
print(majority_element(nums))  # Output: 3
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))  # Output: 2
nums = [1, 2, 3, 4]
print(majority_element(nums))  # Output: -1 (no majority element)
nums = [1, 1, 2, 2, 3, 3, 4, 4]
print(majority_element(nums))  # Output: -1 (no majority element)



# https://leetcode.com/problems/minimum-index-of-a-valid-split/description

def minimumIndex(nums):

    candidate_count, candidate = majority_element(nums)

    left_count = 0

    for i in range(len(nums)):

        if nums[i] == candidate:
            left_count += 1

        right_count = candidate_count - left_count

        # nums[0, ..., i] and nums[i + 1, ..., n - 1] valid split
        if left_count * 2 > i + 1 and right_count * 2 > (len(nums) - i - 1):
            return i

    return -1

# Example usage
nums = [1,2,2,2]
print(minimumIndex(nums))  # Output: 2 (no valid split)
nums = [2,1,3,1,1,1,7,1,2,1]
print(minimumIndex(nums))  # Output: 4 (no valid split)
nums = [3,3,3,3,7,2,2]
print(minimumIndex(nums))  # Output: -1 (no valid split)
