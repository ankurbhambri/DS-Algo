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
    res = 0

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, 2 + left + right)
        return 1 + max(left, right)

    dfs(root)
    return res


def findMaxPathSum(root):
    res = 0

    def dfs(node):
        if not node:
            return 0

        l = max(dfs(node.left), 0)
        r = max(dfs(node.right), 0)
        res = max(res, node.val + l + r)
        return node.val + max(l, r)

    dfs(root)
    return res


def pathSum(root, target):
    def dfs(node):
        if not node:
            return False
        t += node.val
        if not node.left and not node.right:
            return t == target
        return dfs(node.left, t) or dfs(node.right, t)

    return dfs(root, 0)


def sumRoottoLeafNumbers(root):
    def dfs(curr, res):
        if not curr:
            return 0
        res = res * 10 + curr.val
        if not curr.left and not curr.right:
            return res
        return dfs(curr.left, res) + dfs(curr.right, res)

    return dfs(root, 0)


def isSameTree(p, q):

    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


def isSubtree(root, subRoot):
    if not subRoot:
        return True

    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# Traversals
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
    print(findMaxPathSum(root))
