# https://leetcode.com/problems/count-subarrays-with-fixed-bounds

def countSubarrays(nums, minK: int, maxK: int):
    # min_position, max_position: the MOST RECENT positions of minK and maxK.
    # left_bound: the MOST RECENT value outside the range [minK, maxK].
    answer = 0
    min_position = max_position = bad_index = -1
    
    # Iterate over nums, for each number at index i:
    for i, number in enumerate(nums):
        # If the number is outside the range [minK, maxK], update the most recent left_bound.
        if number < minK or number > maxK:
            bad_index = i
            
        # If the number is minK or maxK, update the most recent position.
        if number == minK:
            min_position = i
        if number == maxK:
            max_position = i
            
        # The number of valid subarrays equals the number of elements between left_bound and 
        # the smaller of the two most recent positions.
        answer += max(0, min(min_position, max_position) - bad_index)
        
    return answer

print(countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 1, 7))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 2, 5))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 3, 5))  # Output: 1