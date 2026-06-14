# https://stackoverflow.com/questions/78364596/find-length-of-shortest-substr-that-can-be-removed-from-a-string-resulting-in-a
# https://www.reddit.com/r/AskProgramming/comments/1ca4gcn/shortest_removed_substring_that_results_in_unique/

'''
    Given a string s of length n, the task is to find the length of the shortest substring, 
    which, upon deletion, makes the resultant string consist only of distinct characters.

    A substring is a sequence of characters that appear consecutively within a string. 
    If a substring is deleted, the remaining parts of the string are joined together. 
    If no deletion is necessary, the answer should be 0.

    Example:
    s = "abcbbck"

    There are three optimal choices: "bcb", "bbc", and "bbck".

    The bold characters are the substrings to remove. All result in "abck", which has only distinct characters. 

    The removed substring must have at least 3 characters. Return 3.

    Function Description:

    Complete the function `findShortestSubstring` in the editor with the following parameter:
        - s: the string to analyze

    Returns:
    - int: an integer representing the length of the shortest substring that should be deleted

    Constraints:
        - 1 ≤ n ≤ 10^5
        - s consists of lowercase English letters only.

    Input Format: The first and only line contains the string `s`.

    Sample Case 0:

    Input: s = "xabbcacpqr"

    Output: 3

    Explanation: Given string s = "xabbcacpqr", remove 'bca' to get "xabcpqr".

    Sample Case 1:

    Input: s = "abc"

    Output: 0

    Explanation: The string s = "abc" already contains distinct characters only.
'''

class Solution:
    def findShortestSubstring(self, s: str):

        n = len(s)

        # Agar string pehle se hi unique hai
        if len(set(s)) == n:
            return 0

        # Step 1: Peeche se sabse bada unique suffix dhoodo
        right = n - 1

        seen_suffix = set()

        while right >= 0 and s[right] not in seen_suffix:
            seen_suffix.add(s[right])
            right -= 1
        right += 1 # 'right' ab valid suffix ki shuruat par hai

        # Agar hum poora prefix delete kar dein, toh bachega sirf suffix
        # Is case mein deletion length hogi 'right'
        min_len = right

        # Step 2: Aage se prefix badhao aur check karo
        seen_prefix = set()

        for left in range(n):

            # Agar prefix mein hi duplicate aa gaya, toh aage nahi ja sakte
            if s[left] in seen_prefix:
                break

            seen_prefix.add(s[left])

            # Agar prefix ka character suffix mein bhi hai, 
            # toh suffix ko tab tak chota karo jab tak wo character hat na jaye
            while right < n and s[left] in seen_suffix:
                seen_suffix.remove(s[right])
                right += 1

            # Beech ka jo part delete karna hai uski length: right - left - 1
            min_len = min(min_len, right - left - 1)

        return min_len


print(Solution().findShortestSubstring("a"))  # Output: 0
print(Solution().findShortestSubstring("aa"))  # Output: 1
print(Solution().findShortestSubstring("abc"))  # Output: 0
print(Solution().findShortestSubstring("abcbbck"))  # Output: 3
print(Solution().findShortestSubstring("selection"))  # Output: 1
print(Solution().findShortestSubstring("racingcar"))  # Output: 3
print(Solution().findShortestSubstring("xabbcacpqr"))  # Output: 3
print(Solution().findShortestSubstring("fjyoeekveqsxmjhsftrbzuxmsnnciiyijrtuqqhyphskktvboatbnrmayturngrvgqyclfxfaflccwmgmciacieineaiqxwoiuerfsqcuvggsmaclcokeuyjeegmndpsomtjxumkxwthlludskjxjdjnuhqnxkrjnoarnzgajlhajyynuikajoixwvkxbhcxebujyrxoeqffijyefwlbeeiusyjaubvgxthgllmbkkskqxicaqbpinugldsrzzjemdqiafdynwunouistwinveyylqparpedxixcygdtirxdqqubptimwlxraktkmyrvucvzkiuffshmncmbipzqxrmovyucnnbvdxagzzzxzmzmydkoonojlcgwltnfyocpvbpnvqeouadcdnwvtdehftjsiohxkahwhvncqmzorkponzawkumfxkwaqwtcpksmqggqtsueqxklaqruhkaatxvqftzezocjuvubrdgcehzqtaeftoneapzglcmgbrjlttmephovhxmvbwwmlggmmvjzgpclczmecggpirrgyatowsczrpsvimthwmauzotziixapyoqppjpckxqyzlzlkfcdmvohcioiffcmmaznehmgrghcfpkpmibtinycunxfkygrglxdsyfxwpxcftmnrypzmtrruxyrjcadeocpwfqnsrmlcybqvlpuwaplqufucytooscmtarzxultowpknhgy")) # 712