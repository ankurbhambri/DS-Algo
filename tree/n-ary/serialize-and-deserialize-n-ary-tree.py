# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

from typing import List, Optional


class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            
            res.append(str(node.val))
            
            for child in node.children:
                dfs(child)
            
            res.append("#")  # end of children
        
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str):
        
        if not data:
            return None

        data = data.split(",")
        self.i = 0

        def dfs():
            val = data[self.i]
            self.i += 1

            node = Node(int(val), [])

            while data[self.i] != "#":
                node.children.append(dfs())
            
            self.i += 1  # skip "#"
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))