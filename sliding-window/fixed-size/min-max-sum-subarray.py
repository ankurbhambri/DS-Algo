'''
Calculate the maximum sum of each subarray of size K for a given array..

Time Complexity: O(n)
Space Complexity: O(1) (excluding result list)

# Fixed size sliding window technique

'''
def max_sum_subarray(arr, k):

    max_sum = window_sum = sum(arr[:k])

    for i in range(k, len(arr)):

        window_sum += arr[i] - arr[i-k]   # slide the window
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray([1, 2, 3, 4, 5], 3))  # Output: 12 (subarray [3, 4, 5])
print(max_sum_subarray([1, 2, 3, 4, 5, 6], 4))  # Output: 18 (subarray [3, 4, 5, 6])


'''
Calculate the minimum sum of each subarray of size K for a given array, the most efficient approach is to use the Sliding Window technique.

Time Complexity: O(n)
Space Complexity: O(1) (excluding result list)

'''
def min_sum_subarray(arr, k):
    
    min_sum = window_sum = sum(arr[:k])

    for i in range(k, len(arr)):

        window_sum += arr[i] - arr[i-k]   # slide the window
        min_sum = min(min_sum, window_sum)

    return min_sum

print(min_sum_subarray([1, 2, 3, 4, 5], 3))  # Output: 6
print(min_sum_subarray([1, 2, 3, 4, 5, 6], 4))  # Output: 10
