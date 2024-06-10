"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

"""


def removeDuplicates(s):
    st = []
    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)
    res = ""
    for c in st:
        res += c
    return res


print(removeDuplicates("abbaca"))  # Output: "ca"
print(removeDuplicates("azxxzy"))  # Output: "ay"
