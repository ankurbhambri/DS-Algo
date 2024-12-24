def min_swaps_to_sort(arr):

    n = len(arr)

    indexed_arr = [(val, idx) for idx, val in enumerate(arr)]

    indexed_arr.sort()

    visited = [False] * n
    swaps = 0

    for i in range(n):

        if visited[i] or indexed_arr[i][1] == i:
            continue

        cycle_size = 0
        x = i

        while not visited[x]:
            visited[x] = True
            x = indexed_arr[x][1]
            cycle_size += 1

        swaps += max(cycle_size - 1, 0)

    return swaps


print(min_swaps_to_sort([1, 5, 4, 3, 2]))  # Output: 2
print(min_swaps_to_sort([5, 4, 3, 2, 1]))  # Output: 2
print(min_swaps_to_sort([1, 3, 2]))  # Output: 1
print(min_swaps_to_sort([1, 2, 3, 4]))  # Output: 0
print(min_swaps_to_sort([4, 3, 2, 1]))  # Output: 2
