# https://leetcode.com/problems/custom-sort-string/description/

from collections import Counter

# TC: O(n + m) where n is the length of s and m is the length of order
# SC: O(n) because we are using a HashMap to count characters in s
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        res = ""
        c = Counter(s)

        for i in order:
            res += i * c[i]
            del c[i]

        for k, v in c.items():
            res += (k * v)

        return res

        # Khan's algo
        # adj = {c: [] for c in order + s}
        # indegree = {c: 0 for c in order + s}

        # for i in range(1, len(order)):
        #     indegree[order[i]] += 1
        #     adj[order[i - 1]].append(order[i])

        # visit = set()
        # q = [c for c in s if c in indegree and indegree[c] == 0]

        # while q:

        #     node = q.pop(0)

        #     if node not in s or node in visit:
        #         continue
    
        #     visit.add(node)
        #     res += (node * c[node])

        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        # return res

print(Solution().customSortString("cba", "abcd"))



# Variant: What if we have to optimize your solution from a HashMap<Character, Integer> to a List<Integer>

# TC: O(n + m) where n is the length of s and m is the length of order
# SC: O(1) because we are using a fixed size list of 26 for counting characters

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        res = ""
        c = [0] * 26

        for char in s:
            c[ord(char) - ord('a')] += 1

        for i in order:
            res += i * c[ord(i) - ord('a')]
            c[ord(i) - ord('a')] = 0

        for j in range(26):
            if c[j] > 0:
                res += chr(ord('a') + j) * c[j]

        return res

print(Solution().customSortString("cba", "abcd"))