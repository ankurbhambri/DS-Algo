# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/

'''
Idea: here we have to find the largest lexicographically string that can be formed for number of friends.

So, we have to find the longest string that we can assign to last friend after distributing atleast 1 character to each friend.

In this case, we can use max length formule  -> max_len = total_number_of_characters - (number_of_friends - 1)

Example:
word = "abcdefg"
numFriends = 3
n = 7

→ Minimum 1 char per friend → 3 chars reserved
→ Remaining = 4 chars

→ We can give:

1 char to 2 friends (out of 3)

Then, last friend can get total length of string = 1 + 4 = 5

So max_len = 7 - 3 + 1 = 5 (max length of substring for last friend)

This max_length we need to check from index 0 to n and which ever is lexicographically largest, we will return that)

'''

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # If only one friend, return the word itself
        if numFriends == 1:
            return word

        n = len(word)
        max_substring = ""

        # Maximum length of substring in any split
        max_len = n - numFriends + 1

        # Iterate through the word to find the lexicographically largest substring
        for i in range(n):
            current_substring = word[i:i + max_len]
            print(current_substring, max_len)
            if current_substring > max_substring:
                max_substring = current_substring

        return max_substring
    

print(Solution().answerString("abcde", 3))  # Output: "cde"
print(Solution().answerString("abacaba", 4))  # Output: "caba"
print(Solution().answerString("a", 1))  # Output: "a"
print(Solution().answerString("ab", 2))  # Output: "b"
print(Solution().answerString("abc", 3))  # Output: "c"
