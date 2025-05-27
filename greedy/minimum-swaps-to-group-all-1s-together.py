def minSwaps(nums):

    k = sum(nums)  # nos of ones

    if k == 0:     # if no 1's, no swaps needed
        return 0
    
    n = len(nums)
    max_ones = curr_ones = sum(nums[:k])  # 1’s in first window of size k, Max 1’s
    
    # Window slide
    for i in range(k, n):
        curr_ones -= nums[i - k]  # remove left element 
        curr_ones += nums[i]        # add right element

        max_ones = max(max_ones, curr_ones) # count max 1's in this window
    
    return k - max_ones  # Minimum swaps = total 1’s - max 1’s in any window

print(minSwaps([1, 0, 1, 0, 1]))  # Output: 1
print(minSwaps([0, 0, 0, 1, 1, 1]))  # Output: 0
