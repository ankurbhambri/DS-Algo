def subset_sum(arr_set, target):

    n = len(arr_set)

    new_arr = [[False for i in range(target + 1)] for i in range(n + 1)]

    # Base cndt for column (r-0....n + 1)
    for i in range(n + 1):
        new_arr[i][0] = True

    # Base cndt for row (r-1.....target + 1)
    for i in range(1, target + 1):
        new_arr[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr_set[i - 1] <= j:
                new_arr[i][j] = (
                    new_arr[i][j - arr_set[i - 1]] or new_arr[i - 1][j]
                )
            else:
                new_arr[i][j] = new_arr[i - 1][j]

    return new_arr[n][target]
