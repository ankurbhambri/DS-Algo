# https://www.geeksforgeeks.org/dsa/find-if-there-is-a-subarray-with-0-sum/

# Given an array of positive and negative numbers, the task is to find if there is a subarray (of size at least one) with 0 sum.

# TC: O(N)
# SC: O(N)

def has_zero_sum_subarray(arr):

    seen = set()
    prefix_sum = 0

    for num in arr:

        prefix_sum += num

        if prefix_sum == 0 or prefix_sum in seen:
            return True

        seen.add(prefix_sum)

    return False


print("Zero sum subarray exists:", has_zero_sum_subarray([3, 4, -7, 1, 2, -6]))
print("Zero sum subarray exists:", has_zero_sum_subarray([1, 2, 3, -3, 4]))
print("Zero sum subarray exists:", has_zero_sum_subarray([1, 2, 3, 4, 5]))
print("Zero sum subarray exists:", has_zero_sum_subarray([1, 2, -2, 3, 4]))

# TC: O(N)
# SC: O(N)

# All subarrays with 0 sum, return their start and end indices.
# If there are multiple subarrays with 0 sum, return all of them.

def all_zero_sum_subarrays(arr):

    result = []
    prefix_sum = 0
    prefix_sum_indices = {}

    for i, num in enumerate(arr):

        prefix_sum += num

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in prefix_sum_indices:
            for start_idx in prefix_sum_indices[prefix_sum]:
                result.append((start_idx + 1, i))

        prefix_sum_indices.setdefault(prefix_sum, []).append(i)

    return result


print(all_zero_sum_subarrays([1, 2, 3, 4, 5]))
print(all_zero_sum_subarrays([1, 2, 3, -3, 4]))
print(all_zero_sum_subarrays([1, 2, -2, 3, 4]))
print(all_zero_sum_subarrays([0, -1, 8, -5, -3, -7, 4, 2, 1]))


# Longest Subarray with 0 Sum

def longest_zero_sum_subarray(arr):

    n = len(arr)

    maxLen = 0
    prefixSum = 0
    # prefixSum -> first index
    firstSeen = {}

    # insert prefix sum 0 at index -1
    # to handle sum from start
    firstSeen[0] = -1

    for i in range(n):
        prefixSum += arr[i]

        # prefix sum has been seen before
        if prefixSum in firstSeen:
            idx = firstSeen[prefixSum]
            length = i - idx
            maxLen = max(maxLen, length)
        else:
            # Store first occurrence of this prefix sum
            firstSeen[prefixSum] = i

    return maxLen

print(longest_zero_sum_subarray([1, 2, 3, 4, 5]))
print(longest_zero_sum_subarray([1, 2, 3, -3, 4]))
print(longest_zero_sum_subarray([1, 2, -2, 3, 4]))
print(longest_zero_sum_subarray([0, -1, 8, -5, -3, -7, 4, 2, 1]))
