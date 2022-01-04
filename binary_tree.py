# Binary tree is a non linear data stucture
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            # if data smaller than root
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # if data greater than root
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


def findMaxDiameter(root):

    if root is None:
        return 0

    l = findDiameter(root.left)
    r = findDiameter(root.right)

    temp = max(l, r) + 1
    ans = max(temp, 1 + l + r)
    findDiameter.res = max(findDiameter.res, ans)

    return temp


# This function returns overall maximum path sum in 'res'
# And returns max path sum going through root
def findMaxPathSum(root):

    # Base Condition
    if root is None:
        return 0

    # Hypothesis
    l = findMaxPathSum(root.left)
    r = findMaxPathSum(root.right)

    # Induction
    temp = max(max(l, r) + root.data, root.data)

    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    ans = max(temp, l + r + root.data)

    # Static variable to store the changes
    # Store the maximum result
    findMaxPathSum.res = max(findMaxPathSum.res, ans)

    return temp


# Return maximum path sum in tree with given root
def findMaxSum(root):
    # Initialize result
    findMaxPathSum.res = 0

    # Compute and return result
    findMaxPathSum(root)
    return findMaxPathSum.res


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.data)


if __name__ == "__main__":

    # root = Node(10)
    # root.insert(2)
    # root.insert(10)
    # root.insert(20)
    # root.insert(1)
    # root.insert(-25)
    # root.insert(3)
    # root.insert(4)

    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    print("Print tree")
    root.printTree()

    print("inorder")
    inorder(root)
    print("preorder")
    preorder(root)
    print("postorder")
    postorder(root)
    print("Max path sum in binary tree")
    print(findMaxSum(root))
