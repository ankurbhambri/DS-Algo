# https://codeforces.com/contest/1922/problem/D


class Node:
    def __init__(self, a, d, prev=None, nxt=None):
        self.a = a
        self.d = d
        self.dg = 0
        self.prev = prev
        self.nxt = nxt


class DLL:
    def __init__(self):
        self.left = Node(-1, -1)
        self.right = Node(-1, -1, self.left)
        self.left.nxt = self.right

    def add(self, node):

        prev = self.right.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.right
        self.right.prev = node

    def remove(self, node):
        nxt = node.nxt
        prev = node.prev

        prev.nxt = nxt
        nxt.prev = prev


def berserk_monsters(test_cases):
    res = []
    for n, a, d in test_cases:

        dll = DLL()
        deaths_per_round = []

        for i in range(n):
            dll.add(Node(a[i], d[i]))

        while True:

            cur = dll.left.nxt
            dead = set([dll.left, dll.right])

            while cur != dll.right:
                if cur.prev != dll.left and cur not in dead:
                    cur.prev.dg += cur.a
                if cur.nxt != dll.right and cur not in dead:
                    cur.nxt.dg += cur.a

                cur = cur.nxt

            cur = dll.left.nxt
            dead_nodes = 0
            while cur:
                if cur not in dead and cur.dg > cur.d:
                    dead.add(cur)
                    dll.remove(cur)
                    dead_nodes += 1
                else:
                    cur.dg = 0
                cur = cur.nxt

            deaths_per_round.append(dead_nodes)

            if dead_nodes == 0:
                break

        deaths_per_round.extend([0] * (n - len(deaths_per_round)))
        res.append(deaths_per_round)

    return res


# Input Reading and Output
if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    test_cases = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index : index + n]))
        index += n
        d = list(map(int, data[index : index + n]))
        index += n
        test_cases.append((n, a, d))

    results = berserk_monsters(test_cases)

    for res in results:
        print(" ".join(map(str, res)))

test_cases = [
    (5, [3, 4, 7, 5, 10], [4, 9, 1, 18, 1]),
    (2, [2, 1], [1, 3]),
    (4, [1, 1, 2, 4], [3, 3, 4, 2]),
]
results = berserk_monsters(test_cases)

for result in results:
    print(result)


############################################################################################################
# Another way to solve the problem
############################################################################################################


def solve():

    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))

    left = [i - 1 for i in range(n)]
    right = [i + 1 for i in range(n)]
    right[n - 1] = -1

    v = list(range(n))  # Initialize list of active indices
    vis = [-1] * n  # Visited array to track when nodes are processed

    for i in range(n):
        die = []
        for x in v:
            total_sum = 0
            if left[x] != -1:
                total_sum += a[left[x]]
            if right[x] != -1:
                total_sum += a[right[x]]
            if total_sum > d[x]:
                die.append(x)

        print(len(die), end=" \n" if i == n - 1 else " ")

        v.clear()
        for x in die:
            vis[x] = i

        for x in die:
            if left[x] != -1:
                right[left[x]] = right[x]
                if vis[left[x]] < i:
                    v.append(left[x])
                    vis[left[x]] = i
            if right[x] != -1:
                left[right[x]] = left[x]
                if vis[right[x]] < i:
                    v.append(right[x])
                    vis[right[x]] = i


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
