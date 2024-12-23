def next_smaller_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


arr = [4, 8, 5, 2, 25]
print(next_smaller_element(arr))  # Output: [2, 5, 2, -1, -1]
