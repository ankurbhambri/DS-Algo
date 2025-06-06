# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, sentence: str) -> str:
        # Convert the string to a list of characters for in-place manipulation
        sentence = list(sentence)
        str_len = len(sentence)

        # Helper function to reverse a portion of the list in-place
        def helper(s: list[str], left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire list
        helper(sentence, 0, str_len - 1)

        # Step 2: Reverse each word in the list
        start = 0
        for end in range(str_len + 1):
            if end == str_len or sentence[end] == ' ':
                print(start, end - 1, str_len, sentence, sentence[end])
                helper(sentence, start, end - 1)
                start = end + 1

        # Step 3: Join the list back into a string and return
        return ''.join(sentence)

print(Solution().reverseWords("the sky is blue"))  # "blue is sky the"
print(Solution().reverseWords("  hello world  "))  # "world hello"
print(Solution().reverseWords("a good   example"))  # "example good a"
print(Solution().reverseWords("  Bob    Loves  Alice   "))  # "Alice Loves Bob"
print(Solution().reverseWords("Alice does not even like bob"))  # "bob like even not does Alice"