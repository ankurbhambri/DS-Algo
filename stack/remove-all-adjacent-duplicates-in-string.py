# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        val = ""
        st = []
        for ch in s:
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)

print(Solution().removeDuplicates("abbaca"))
print(Solution().removeDuplicates("azxxzy"))
print(Solution().removeDuplicates("aababaab"))


# VARIANT: What if you had to remove all adjacent duplicates as you iterate left-to-right?

def remove_all_adjacent_duplicates_variant(s: str) -> str:
    # stack elements: [char, freq]
    stack = []

    for ch in s:

        if not stack:
            stack.append([ch, 1])
            continue

        # same character → increase frequency
        if stack[-1][0] == ch:
            stack[-1][1] += 1
            continue

        # different character → finalize previous run
        if stack[-1][1] > 1:
            stack.pop()

        # now handle current character (possible chain reaction)
        if not stack or stack[-1][0] != ch:
            stack.append([ch, 1])
        else:
            stack[-1][1] += 1

    # final cleanup
    if stack and stack[-1][1] > 1:
        stack.pop()

    # build result
    return "".join(ch for ch, _ in stack)


print(remove_all_adjacent_duplicates_variant("azxxzy"))
print(remove_all_adjacent_duplicates_variant("abbbacxdd"))