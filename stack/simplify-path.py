# https://leetcode.com/problems/simplify-path/description/


class Solution:
    def simplifyPath(self, path: str) -> str:

        curr = ""
        stack = []

        for c in path + '/':
            if c == '/':
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""  
            else:
                curr += c

        return '/' + '/'.join(stack)


print(Solution().simplifyPath("/../"))  # "/"
print(Solution().simplifyPath("/a/./b/../../c/"))  # "/c"
print(Solution().simplifyPath("/home//foo/"))  # "/home/foo"
print(Solution().simplifyPath("/a//b////c/d//././/.."))  # "/a/b/c"