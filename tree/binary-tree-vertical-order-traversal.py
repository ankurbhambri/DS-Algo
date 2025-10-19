from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_order_traversal(root):

    if not root:
        return
    
    col_map = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column)

    l, r = float("inf"), float("-inf")

    while queue:

        node, col = queue.popleft()
        col_map[col].append(node.val)

        l = min(l, col)
        r = max(r, col)

        if node.left:
            queue.append((node.left, col - 1))

        if node.right:
            queue.append((node.right, col + 1))

    for col in range(l, r + 1):
        for val in col_map[col]:
            print(val, end=" ")


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(3)
root.right.right = Node(7)

print(vertical_order_traversal(root))
