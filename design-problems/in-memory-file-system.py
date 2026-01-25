# https://leetcode.com/problems/design-in-memory-file-system/description/

'''
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. 
If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. 
If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. 
If the file already exists, you need to append given content to original content. This function has void return type.

function readContentFromFile(): Given a file path, return its content in string format.

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]

'''

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
