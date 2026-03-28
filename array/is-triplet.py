def is_triplet(arr):
    n = len(arr)

    # Create a set to store the squares of elements in the array
    square_set = set()
    for num in arr:
        square_set.add(num * num)

    # Fix one element (c^2) and find other two elements (a^2, b^2) using two pointers
    for i in range(n):
        for j in range(i + 1, n):
            c_square = arr[i] * arr[i] + arr[j] * arr[j]
            if c_square in square_set:
                return "Yes" # Triplet found

    return "No" # Triplet not found


# Additional test cases
test_cases = [
    ([3, 2, 4, 6, 5], "Yes"),  # Example test case
    ([5, 12, 13, 15, 20], "Yes"),  # Test case with a triplet in the array
    ([7, 24, 25, 10, 8], "Yes"),  # Test case with a triplet in the array
    ([8, 15, 17, 10, 21], "Yes"),  # Test case with a triplet in the array
    ([1, 2, 3, 5, 5], "No"),  # Test case with no triplet in the array
    ([6, 8, 10, 15, 20], "No"),  # Test case with no triplet in the array
]

# Run tests
for arr, expected_result in test_cases:
    result = is_triplet(arr)
    print(f"Array: {arr}, Expected Result: {expected_result}, Actual Result: {result}")
