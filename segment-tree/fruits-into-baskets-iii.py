# https://leetcode.com/problems/fruits-into-baskets-iii


# TC: O(n log m), where n is the number of fruits and m is the number of baskets
# SC: O(m) for the segment tree
class SegmentTree:
    def __init__(self, n):

        self.tree = [float("-inf")] * (4 * n)

        if n > 0:
            self.build(0, 0, n - 1)

    # 1. Tree Build Karne ka Function
    def build(self, node, start, end):

        if start == end:
            # Leaf node: actual array element store karo
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        # Left aur Right subtrees ko build karo
        self.build(left_child, start, mid)

        self.build(right_child, mid + 1, end)

        # Parent node ko update karo
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])


    # Thoda sa different hai kyunki hum yahan pe ek specific fruit ko query kar rahe hain
    # Hum yeh dekh rahe hain ki kaunsa basket is fruit ko rakh sakta hai (yaani ki basket ka capacity fruit se bada ya barabar hona chahiye)
    # Agar koi basket nahi hai jo is fruit ko rakh sake, toh hum -1 return karenge
    # Agar koi basket hai, toh hum uska index return karenge.
    def query(self, node, start, end, fruit):

        if self.tree[node] < fruit:
            return -1

        if start == end:
            return start

        mid = (start + end) // 2

        left = 2 * node + 1

        right = 2 * node + 2

        if self.tree[left] >= fruit:
            return self.query(left, start, mid, fruit)

        return self.query(right, mid + 1, end, fruit)

    # 3. Point Update Function (Index par value badalna)
    def update(self, node, start, end, idx, val):

        if start == end:
            # Leaf node par nayi value update karo
            self.arr[idx] = val
            self.tree[node] = val
            return

        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        if start <= idx <= mid:
            # Agar index left side mein hai
            self.update(left_child, start, mid, idx, val)
        else:
            # Agar index right side mein hai
            self.update(right_child, mid + 1, end, idx, val)

        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:

        m = len(baskets)

        if m == 0:
            return len(fruits)

        tree = SegmentTree(m)

        count = 0

        for fruit in fruits:

            idx = tree.query(0, 0, m - 1, fruit)

            if idx != -1:
                tree.update(0, 0, m - 1, idx, float("-inf"))
                count += 1

        return len(fruits) - count


print(Solution().numOfUnplacedFruits([1, 2, 3, 4, 5], [2, 3, 4]))  # Example usage
print(Solution().numOfUnplacedFruits([1, 2, 3], [1, 2, 3]))  # Example usage
print(Solution().numOfUnplacedFruits([1, 2, 3], [4, 5, 6]))  # Example usage
print(Solution().numOfUnplacedFruits([], [1, 2, 3]))  # Example usage
