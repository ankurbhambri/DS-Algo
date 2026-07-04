class DisjointSet:
    def __init__(self, n):

        self.n = n
        # initially every noe rank is 0
        self.rank = [1] * n
        # initially every node is its own parent
        self.parent = list(range(n))


    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


    def union(self, node1, node2):

        p1 = self.find(node1)
        p2 = self.find(node2)

        # Same parent, if both nodes parent are same then union is not possible
        if p1 == p2:
            print("")
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2

        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1

        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


if __name__ == "__main__":

    uf = DisjointSet(10)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)

    uf.union(2, 4)  # not possible to union because same parent

    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(7, 8)
    uf.union(8, 9)

    print(uf.find(2))  # output: 0 -> connected to 1 but 1 itself parent is 0.
    print(uf.find(4))  # output: 0 -> connected to 3 -> 2 -> 1 -> 0.
    print(uf.find(9))  # output: 6 -> 8 -> 7 -> 6

    print(uf.find(1) == uf.find(2))  # True because their parents are same 0

    print(uf.find(4) == uf.find(9))  # False because their parents are different

    print(uf.parent, uf.rank)


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

class Solution:
    def removeStones(self, stones):

        parent = {x: x for x, y in stones}

        max_row = max(x for x, y in stones) + 1

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)        

        for x, y in stones:
            union(x, y + max_row + 1)

        res = set()
        for x, y in stones:
            res.add(find(x))

        return len(stones) - len(res)


# https://leetcode.com/problems/lexicographically-smallest-equivalent-string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # Each character 'a' to 'z' represented by index 0 to 25
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):

            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        res = ""
        for x in baseStr:
            val = ord(x) - ord("a")
            res += chr(find(val) + ord("a"))

        return res


print(Solution().smallestEquivalentString("parker", "morris", "parser"))  # Output: "makkek"
print(Solution().smallestEquivalentString("hello", "world", "hold"))  # Output: "hdld"
print(Solution().smallestEquivalentString("leetcode", "programs", "sourcecode"))  # Output: "aauaaaa"
print(Solution().smallestEquivalentString("abc", "cde", "fgh"))  # Output: "fgh"


# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/


# TC: O(ElogE + QlogQ + (E+Q) * α(N)) where E is the number of edges, Q is the number of queries, N is the number of nodes, and α is the inverse Ackermann function.
# SC: O(N) for the DSU data structure.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # Step 1: DSU initialize karna
        dsu = DSU(n)

        # Step 2: Queries ka original index track karna kyunki humein ans usi order mein chahiye
        # queries_with_index = [[p, q, limit, original_index], ...]
        queries_with_index = []
        for i, q in enumerate(queries):
            queries_with_index.append([q[0], q[1], q[2], i])

        # Step 3: Edges aur Queries dono ko sort karna (Weights and Limits ke basis par)
        edgeList.sort(key=lambda x: x[2])
        queries_with_index.sort(key=lambda x: x[2])

        ans = [False] * len(queries)
        edge_idx = 0

        # Step 4: Process Queries One by One
        for p, q, limit, original_idx in queries_with_index:

            # Jab tak edge ka weight limit se chhota hai, unhe DSU mein connect karte jao
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, w = edgeList[edge_idx]
                dsu.union(u, v)
                edge_idx += 1

            # Check karo kya p aur q ab connected hain
            if dsu.find(p) == dsu.find(q):
                ans[original_idx] = True
            else:
                ans[original_idx] = False

        return ans


print(Solution().distanceLimitedPathsExist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]))  # Output: [False, True]
print(Solution().distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]))  # Output: [True, False]