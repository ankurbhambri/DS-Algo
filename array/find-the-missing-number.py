def missingNum(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expSum = n * (n + 1) // 2

    # Return the missing number
    return expSum - totalSum

print(missingNum([8, 2, 4, 5, 3, 7, 1])) # 6
print(missingNum([1, 2, 3, 5]))  # 4