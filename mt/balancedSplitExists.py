def balancedSplitExists(arr):
    arr.sort()
    total_sum = sum(arr)

    left_sum = 0
    for i in range(len(arr) - 1):
        left_sum += arr[i]
        right_sum = total_sum - left_sum

        if left_sum == right_sum and arr[i] < arr[i + 1]:
            return True

    return False


print(balancedSplitExists([1, 5, 7, 1]))
