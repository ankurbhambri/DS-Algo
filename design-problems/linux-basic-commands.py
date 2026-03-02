# https://codezym.com/question/14
# https://leetcode.com/problems/design-in-memory-file-system/description/
# https://leetcode.com/discuss/post/369272/amazon-onsite-linux-find-command-by-anon-numt/

from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def matches(self, name: str, size: int, content: str, criteria: str) -> bool:
        pass

class SizeStrategy(SearchStrategy):
    def matches(self, name, size, content, criteria):
        return size > int(criteria)

class ExtensionStrategy(SearchStrategy):
    def matches(self, name, size, content, criteria):
        return name.endswith(criteria)

class ContentStrategy(SearchStrategy):
    def matches(self, name, size, content, criteria):
        return criteria in content

class FileNode:
    def __init__(self, name, is_dir=True):
        self.name = name
        self.is_dir = is_dir
        self.children = {}  # Trie nodes
        self.content = ""   # For files
        self.size = 0       # Simplified size tracking

class FileSystem:
    def __init__(self):
        self.root = FileNode("/")
        self.strategies = {
            1: SizeStrategy(),
            2: ExtensionStrategy(),
            3: ContentStrategy()
        }

    def _get_path_list(self, path: str):
        return [p for p in path.split("/") if p]

    def mkdir(self, path: str):
        curr = self.root
        for part in self._get_path_list(path):
            if part not in curr.children:
                curr.children[part] = FileNode(part, is_dir=True)
            curr = curr.children[part]
        return f"Directory {path} created/exists."

    def write(self, path: str, content: str):
        parts = self._get_path_list(path)
        curr = self.root
        # Navigate to the parent directory
        for part in parts[:-1]:
            if part not in curr.children:
                curr.children[part] = FileNode(part, is_dir=True)
            curr = curr.children[part]
        
        # Handle the file
        file_name = parts[-1]
        if file_name not in curr.children:
            curr.children[file_name] = FileNode(file_name, is_dir=False)

        node = curr.children[file_name]
        node.content += content
        node.size = len(node.content)
        return f"Written to {path}. New size: {node.size}"

    def read(self, path: str):
        curr = self.root
        for part in self._get_path_list(path):
            if part not in curr.children:
                return "Error: Path not found"
            curr = curr.children[part]
        return curr.content if not curr.is_dir else f"Error: {path} is a directory"

    def ls(self, path: str):
        curr = self.root
        if path != "/":
            for part in self._get_path_list(path):
                if part not in curr.children: return []
                curr = curr.children[part]
        
        return sorted(list(curr.children.keys()))


    def search(self, strategy_id: int, start_path: str, criteria: str):
        strategy = self.strategies.get(strategy_id)
        if not strategy: return []

        # Find starting node
        curr = self.root
        if start_path != "/":
            for part in self._get_path_list(start_path):
                if part not in curr.children: return []
                curr = curr.children[part]

        results = []
        self._dfs_search(curr, start_path.rstrip("/"), strategy, criteria, results)
        return sorted(results)

    def _dfs_search(self, node, current_path, strategy, criteria, results):
        # If it's a file, check matches
        if not node.is_dir:
            if strategy.matches(node.name, node.size, node.content, criteria):
                results.append(f"{current_path}")
            return

        # If it's a directory, recurse
        for name, child_node in node.children.items():
            new_path = f"{current_path}/{name}"
            self._dfs_search(child_node, new_path, strategy, criteria, results)



fs = FileSystem()

# Perform Linux commands
fs.mkdir("/home/ubuntu/docs")
fs.write("/home/ubuntu/docs/resume.pdf", "Experience in Python...")
fs.write("/home/ubuntu/docs/notes.txt", "Learning Trie algorithms.")
fs.write("/home/ubuntu/image.jpg", "binary_data_here")

print("LS /home/ubuntu/docs:", fs.ls("/home/ubuntu/docs"))
print("Read File:", fs.read("/home/ubuntu/docs/notes.txt"))

# Perform Search
print("\n--- Search Results ---")
# Search for files > 10 bytes in /home
print("Size > 10 in /home:", fs.search(1, "/home", "10"))
# Search for .pdf extension
print("Extension .pdf:", fs.search(2, "/", ".pdf"))
# Search for content containing 'Python'
print("Content 'Python':", fs.search(3, "/home", "Python"))