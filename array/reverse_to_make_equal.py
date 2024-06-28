def areTheyEqualWithIndices(arr_a, arr_b):

    if len(arr_a) != len(arr_b):
        return False, []

    reversals = []

    def reverse_subarray(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Traverse the arrays
    i = 0
    while i < len(arr_a):
        if arr_a[i] != arr_b[i]:

            j = i
            while j < len(arr_b) and arr_b[j] != arr_a[i]:
                j += 1

            if j < len(arr_b):

                reverse_subarray(arr_b, i, j)
                reversals.append((i, j))
            else:
                return False, []
        i += 1

    return arr_a == arr_b, reversals


# Time complexity: O(n^2)
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output, reversals = areTheyEqualWithIndices(A, B)
print("Output:", output)
print("Reversals:", reversals)
