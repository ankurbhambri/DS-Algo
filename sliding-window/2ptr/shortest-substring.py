# https://stackoverflow.com/questions/78364596/find-length-of-shortest-substr-that-can-be-removed-from-a-string-resulting-in-a
# https://www.reddit.com/r/AskProgramming/comments/1ca4gcn/shortest_removed_substring_that_results_in_unique/

"""
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

    Input Format:
    The first and only line contains the string `s`.

    Sample Case 0:
    Input:
    s = "xabbcacpqr"

    Output:
    3

    Explanation:
    Given string s = "xabbcacpqr", remove 'bca' to get "xabcpqr".

    Sample Case 1:
    Input:
    s = "abc"

    Output:
    0

    Explanation:
    The string s = "abc" already contains distinct characters only.
"""

from collections import Counter

def findShortestSubstring(s):

    n = len(s)

    char_count = Counter(s)

    # characters appear more than once
    duplicates = {char for char, count in char_count.items() if count > 1}

    if len(duplicates) == 0:
        return 0

    l = 0
    freq = {}
    min_length = n

    for r in range(n):

        if s[r] in duplicates:
            freq[s[r]] = freq.get(s[r], 0) + 1

        # Try to contract window from left
        while l <= r:
            # Check if current window contains enough duplicates to remove
            # We need (char_count[char] - 1) occurrences of each duplicate char
            can_contract = True
            for char in duplicates:
                if freq.get(char, 0) < char_count[char] - 1:
                    can_contract = False
                    break

            if can_contract:

                # Current window is valid, update minimum length
                min_length = min(min_length, r - l + 1)

                # Try to contract from left
                if s[l] in freq:
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        del freq[s[l]]
                l += 1
            else:
                break

    return min_length

print(findShortestSubstring("a"))  # Output: 0
print(findShortestSubstring("aa"))  # Output: 1
print(findShortestSubstring("abc"))  # Output: 0
print(findShortestSubstring("abcbbck"))  # Output: 3
print(findShortestSubstring("selection"))  # Output: 1
print(findShortestSubstring("racingcar"))  # Output: 3
print(findShortestSubstring("xabbcacpqr"))  # Output: 3
print(findShortestSubstring("fjyoeekveqsxmjhsftrbzuxmsnnciiyijrtuqqhyphskktvboatbnrmayturngrvgqyclfxfaflccwmgmciacieineaiqxwoiuerfsqcuvggsmaclcokeuyjeegmndpsomtjxumkxwthlludskjxjdjnuhqnxkrjnoarnzgajlhajyynuikajoixwvkxbhcxebujyrxoeqffijyefwlbeeiusyjaubvgxthgllmbkkskqxicaqbpinugldsrzzjemdqiafdynwunouistwinveyylqparpedxixcygdtirxdqqubptimwlxraktkmyrvucvzkiuffshmncmbipzqxrmovyucnnbvdxagzzzxzmzmydkoonojlcgwltnfyocpvbpnvqeouadcdnwvtdehftjsiohxkahwhvncqmzorkponzawkumfxkwaqwtcpksmqggqtsueqxklaqruhkaatxvqftzezocjuvubrdgcehzqtaeftoneapzglcmgbrjlttmephovhxmvbwwmlggmmvjzgpclczmecggpirrgyatowsczrpsvimthwmauzotziixapyoqppjpckxqyzlzlkfcdmvohcioiffcmmaznehmgrghcfpkpmibtinycunxfkygrglxdsyfxwpxcftmnrypzmtrruxyrjcadeocpwfqnsrmlcybqvlpuwaplqufucytooscmtarzxultowpknhgy")) # 712
