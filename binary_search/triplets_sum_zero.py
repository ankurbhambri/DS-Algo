# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/


def findTriplets(arr):

    n = len(arr)
    result = []
    arr.sort()
    
    for i in range(n-2):

        left = i + 1
        right = n - 1
        
        while left < right:

            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif curr_sum < 0:
                left += 1

            else:
                right -= 1
    
    return result


# Test cases
print(findTriplets([0, -1, 2, -3, 1]))  # Output: [[-3, 1, 2], [-1, 0, 1]]
print(findTriplets([1, -2, 1, 0, 5]))  # Output: [[-2, 1, 1]]
print(findTriplets([2, 3, 1, 0, 5]))  # Output: []
