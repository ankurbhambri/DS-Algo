# TC - O(n)
# SC - O(1)


def is_consecutive(arr):
    if not arr:
        return False

    # Find minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Check the length of the array
    if len(arr) != (max_val - min_val + 1):
        return False

    # Check for duplicates by comparing lengths of the list and set
    if len(arr) != len(set(arr)):
        return False

    return True


arr1 = [3, 4, 2, 5, 1]
arr2 = [1, 2, 4, 5]

print(is_consecutive(arr1))
print(is_consecutive(arr2))


# TC - O(n)
# SC - O(N)


def is_consecutive(arr):
    if not arr:
        return False

    min_val = float("inf")
    max_val = float("-inf")
    seen = set()

    for num in arr:
        if num in seen:
            return False  # Duplicate found
        seen.add(num)

        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # Check if the length of the array matches the expected length
    if len(arr) != (max_val - min_val + 1):
        return False

    return True


# Example usage
arr1 = [3, 4, 2, 5, 1]
arr2 = [1, 2, 4, 5]

print(is_consecutive(arr1))  # Should return True
print(is_consecutive(arr2))  # Should return False
