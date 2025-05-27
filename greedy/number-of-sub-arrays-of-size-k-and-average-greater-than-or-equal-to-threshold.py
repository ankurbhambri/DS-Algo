# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

# Formula
# x = sum(k length subarry)
# x / k = threshold
# x = k * threshold

def numOfSubarrays(arr, k, threshold):

    target = k * threshold
    cur_sum = sum(arr[:k])
    c = 1 if cur_sum >= target else 0

    for i in range(k, len(arr)):
        cur_sum += arr[i] - arr[i - k]
        if cur_sum >= target:
            c += 1
    return c


print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))  # Output: 3
print(numOfSubarrays([1,2,3,4,5], 1, 2))  # Output: 4
print(numOfSubarrays([1,2,3,4,5], 2, 3))  # Output: 2
print(numOfSubarrays([1,2,3,4,5], 3, 4))  # Output: 1
