# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):

        data = data.split(",")
        self.i = 0

        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(data[self.i]))

            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


obj = TreeNode(1)
obj.left = TreeNode(2)
obj.right = TreeNode(3)
obj.left.left = TreeNode(4)
obj.left.right = TreeNode(5)
codec = Codec()
serialized = codec.serialize(obj)
print("Serialized:", serialized)
deserialized = codec.deserialize(serialized)
print("Deserialized:", deserialized.val)  # Should print the root value of the deserialized tree
