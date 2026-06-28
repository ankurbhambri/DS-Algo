# Here we are doing Range Query and Point Update
class SegmentTree:
    def __init__(self, arr):

        self.arr = arr

        self.n = len(arr)

        # Segment tree ka size max 4 * N hota hai
        self.tree_min = [float("inf")] * (4 * self.n)
        self.tree_max = [float("-inf")] * (4 * self.n)

        if self.n > 0:
            self._build(0, 0, self.n - 1)

    # 1. Tree Build Karne ka Function
    def _build(self, node, start, end):

        if start == end:
            # Leaf node: actual array element store karo
            self.tree_min[node] = self.arr[start]
            self.tree_max[node] = self.arr[start]
            return

        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        # Left aur Right subtrees ko build karo
        self._build(left_child, start, mid)

        self._build(right_child, mid + 1, end)

        # Parent node ko update karo
        self.tree_min[node] = min(self.tree_min[left_child], self.tree_min[right_child])
        self.tree_max[node] = max(self.tree_max[left_child], self.tree_max[right_child])

    # 2. Range Maximum Query Function
    def query(self, node, start, end, l, r):

        # Case 1: No Overlap (Query range completely bahar hai)
        if r < start or end < l:
            return float('inf'), float('-inf') # Neutral values for min and max

        # Case 2: Complete Overlap (Current range query range ke andar hai)
        if l <= start and end <= r:
            return self.tree_min[node], self.tree_max[node]

        # Case 3: Partial Overlap
        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        left_mn, left_mx = self.query(left_child, start, mid, l, r)

        right_mn, right_mx = self.query(right_child, mid + 1, end, l, r)

        return min(left_mn, right_mn), max(left_mx, right_mx)

    # 3. Point Update Function (Index par value badalna)
    def update(self, node, start, end, idx, val):

        if start == end:
            # Leaf node par nayi value update karo
            self.arr[idx] = val
            self.tree_min[node] = val
            self.tree_max[node] = val
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

        self.tree_min[node] = min(self.tree_min[left_child], self.tree_min[right_child])
        self.tree_max[node] = max(self.tree_max[left_child], self.tree_max[right_child])


arr = [1, 3, 2, 8]

# Segment tree initialize karein
seg_tree = SegmentTree(arr)

# Range [0, 2] yaani (1, 3, 2) ka max nikaalein
print("Min an Max in range [0, 2]:", seg_tree.query(0, 0, len(arr)-1, 0, 2)) # Output: (1, 3)

# Range [1, 3] yaani (3, 2, 8) ka max nikaalein
print("Min and Max in range [1, 3]:", seg_tree.query(0, 0, len(arr)-1, 1, 3)) # Output: (2, 8)

# Index 3 ki value ko 8 se badalkar 0 kar dete hain
print("\nUpdating index 3 to 0...")
seg_tree.update(0, 0, len(arr)-1, 3, 0)

# Ab poore array [1, 3, 2, 0] ka max nikaalein
print("New Min and Max in range [0, 3]:", seg_tree.query(0, 0, len(arr)-1, 0, 3)) # Output: (0, 3)