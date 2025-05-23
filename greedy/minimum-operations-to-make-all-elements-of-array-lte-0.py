# number of unique positive values = minimum operations required.

def min_operations(arr):
    unique_positive = set(x for x in arr if x > 0)
    return len(unique_positive)

# Example
arr = [5, 1, 1, 2, 3]
print(min_operations(arr))  # Output: 4
