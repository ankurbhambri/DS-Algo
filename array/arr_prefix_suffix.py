def calculate_prefix_suffix_sums(arr):
    n = len(arr)

    # Initialize prefix and suffix sum arrays
    prefix_sum = [0] * n
    suffix_sum = [0] * n

    # Calculate prefix sums
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Calculate suffix sums
    suffix_sum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    return prefix_sum, suffix_sum


# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum, suffix_sum = calculate_prefix_suffix_sums(arr)
print("Prefix Sum:", prefix_sum)
print("Suffix Sum:", suffix_sum)
