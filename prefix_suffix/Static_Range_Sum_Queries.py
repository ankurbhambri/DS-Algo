# https://cses.fi/problemset/task/1646


def solution(arr, q):

    res = []
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    for a, b in q:
        res.append(arr[b] - arr[a - 1])

    return res


arr = [3, 2, 4, 5, 1, 1, 5, 3]
q = [[2, 4], [5, 6], [1, 8], [3, 3]]
print(solution(arr, q))
