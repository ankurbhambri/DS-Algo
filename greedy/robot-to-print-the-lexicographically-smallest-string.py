# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

'''
    Just keep count of the frequency of every char to go in lexicographic order. 
    Then add char one by one to the stack , if the lowest lexicgraphic char is greater than equal to element on top of stack, 
    add the top of stack to ans. At last if the stack isn't empty after traversing all elements, add all elemrnts to the ans.
'''

class Solution:
    def robotWithString(self, s: str) -> str:

        st = []
        res = ""
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1

        def helper():
            for i in range(26):
                if freq[i] != 0:
                    return chr(ord("a") + i)
            return "a"

        for c in s:

            st.append(c)

            freq[ord(c) - ord("a")] -= 1

            val = helper() # lowest lexicgraphic char 
 
            # If lowest lexicgraphic char, is greater than equal to element on top of stack, pop and add it to the res.
            while st and st[-1] <= val:
                res += st.pop()

        while st:
            res += st.pop()

        return res


print(Solution().robotWithString("zza"))  # "azz"
print(Solution().robotWithString("bac"))  # "abc"
print(Solution().robotWithString("bdda"))  # "abdd"
print(Solution().robotWithString("cba"))  # "abc"
