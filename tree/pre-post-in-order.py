# Definition of a binary tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

# Sample Tree:
#        A
#       / \
#      B   C
#     / \
#    D   E

# Building the tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print("Preorder Traversal:")
preorder(root)  # Output: A B D E C

print("\nInorder Traversal:")
inorder(root)   # Output: D B E A C

print("\nPostorder Traversal:")
postorder(root) # Output: D E B C A
