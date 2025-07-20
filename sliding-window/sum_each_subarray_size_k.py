'''
Calculate the sum of each subarray of size K for a given array, the most efficient approach is to use the Sliding Window technique.

Time Complexity: O(n)
Space Complexity: O(1) (excluding result list)

'''

def sum_of_subarrays(arr, k):

    n = len(arr)

    if k > n:
        return []

    result = []
    window_sum = sum(arr[:k])  # sum of first window
    result.append(window_sum)

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum)

    return result


print(sum_of_subarrays([1, 2, 3, 4, 5], 2))  # Output: [3, 5, 7, 9]
print(sum_of_subarrays([1, 2, 3, 4, 5], 3))  # Output: [6, 9, 12]
