'''

    Given an array arr[], an integer K and a Sum. The task is to check if there exists any subarray with K elements whose sum is equal to the given sum. 
    If any of the subarray with size K has the sum equal to the given sum then print YES otherwise print NO.

'''

# TC: O(N)
# SC: O(1)

def has_subarray_with_sum(arr, k, target_sum):
    n = len(arr)
    
    # If K is larger than array size, no such subarray can exist
    if k > n:
        return "NO"
    
    # Compute the sum of the first window of size K
    window_sum = sum(arr[:k])
    
    # Check if the first window matches the target
    if window_sum == target_sum:
        return "YES"
    
    # Slide the window across the array
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum == target_sum:
            return "YES"
    
    return "NO"


print(has_subarray_with_sum([1, 2, 3, 4, 5], 3, 6))  # YES
print(has_subarray_with_sum([1, 2, 3, 4, 5], 2, 8))  # NO
print(has_subarray_with_sum([1, 2, 3, 4, 5], 5, 15)) # YES
print(has_subarray_with_sum([1, 2, 3, 4, 5], 1, 1))   # YES