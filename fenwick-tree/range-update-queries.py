# https://cses.fi/problemset/task/1651


def solve(values, queries):

    n = len(values)
    x = [0] + list(values)
    tree = [0] * (n + 2)

    def add(index: int, delta: int) -> None:
        while index <= n:
            tree[index] += delta
            index += index & -index

    def point_query(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    for i in range(1, n + 1):
        diff = x[i] - x[i - 1]
        add(i, diff)

    output = []
    for query in queries:

        if query[0] == 1:
            _, left, right, delta = query
            add(left, delta)
            add(right + 1, -delta)

        elif query[0] == 2:
            _, index = query
            output.append(point_query(index))

    return output

print(solve([1, 2, 3], [[1, 1, 2, 1], [2, 2], [2, 3]]))  # [3, 3]
print(solve([3, 2, 4, 5, 1, 1, 5, 3], [[2, 4], [1, 2, 5, 1], [2, 4]]))  # [5, 6]