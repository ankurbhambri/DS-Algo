class Node:
    def __init__(self):
        self.is_file = False
        self.children = {}  # name -> Node
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()

    def _traverse(self, path: str) -> Node:
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")
        for part in parts:
            if not part:
                continue
            if part not in curr.children:
                curr.children[part] = Node()
            curr = curr.children[part]
        return curr

    def ls(self, path: str) -> list[str]:
        node = self._traverse(path)
        if node.is_file:
            return [path.split("/")[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content

fs = FileSystem()

fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.ls("/"))           # ["a"]
print(fs.ls("/a/b/c"))      # ["d"]
print(fs.readContentFromFile("/a/b/c/d"))  # "hello"
