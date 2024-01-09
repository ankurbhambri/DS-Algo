def is_triplet(arr):
    n = len(arr)

    # Square all elements in the array
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    # Sort the squared array
    arr.sort()

    # Fix one element (c^2) and find other two elements (a^2, b^2) using two pointers
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] == arr[i]:
                return "Yes"  # Triplet found
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1

    return "No"  # Triplet not found


# Example usage:
arr = [3, 2, 4, 6, 5]
result = is_triplet(arr)
print("Output:", result)
