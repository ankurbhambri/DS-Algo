# https://stackoverflow.com/questions/78364596/find-length-of-shortest-substr-that-can-be-removed-from-a-string-resulting-in-a

"""
    Determine the length of the shortest substring to delete from a string of length n, 
    so that the resulting string contains only distinct characters.

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

# def findShortestSubstring(s):
#     n = len(s)
    
#     # Check if string already has all distinct characters
#     if len(set(s)) == n:
#         return 0
    
#     # Count frequency of each character
#     char_count = {}
#     for c in s:
#         char_count[c] = char_count.get(c, 0) + 1
    
#     # Find characters that appear more than once
#     duplicates = set()
#     for char, count in char_count.items():
#         if count > 1:
#             duplicates.add(char)
    
#     min_length = n
    
#     # Use sliding window to find shortest substring containing all duplicates
#     for left in range(n):
#         seen_duplicates = set()
        
#         for right in range(left, n):
#             if s[right] in duplicates:
#                 seen_duplicates.add(s[right])
            
#             # If current window contains all duplicate characters
#             if seen_duplicates == duplicates:
#                 # Check if removing this window results in distinct characters
#                 remaining = s[:left] + s[right+1:]
#                 if len(set(remaining)) == len(remaining):
#                     min_length = min(min_length, right - left + 1)
#                 break
    
#     return min_length

def findShortestSubstring(s):

    n = len(s)
    
    # Quick check: if already all unique characters
    if len(set(s)) == n:
        return 0

    l = 0
    res = n  # Start with max possible length

    # Use right pointer for sliding window
    for r in range(n):
        # Check if prefix and suffix are disjoint
        combined = s[:l] + s[r+1:]
        if len(set(combined)) == len(combined):
            # All unique after removing s[l:r+1]
            res = min(res, r - l + 1)
            # Try to shrink from l
            while l <= r:
                combined = s[:l+1] + s[r+1:]
                if len(set(combined)) == len(combined):
                    res = min(res, r - l)
                    l += 1
                else:
                    break
    return res

print(findShortestSubstring("a"))  # Output: 0
print(findShortestSubstring("aa"))  # Output: 1
print(findShortestSubstring("abc"))  # Output: 0
print(findShortestSubstring("abcbbck"))  # Output: 3
print(findShortestSubstring("xabbcacpqr"))  # Output: 3
print(findShortestSubstring("fjyoeekveqsxmjhsftrbzuxmsnnciiyijrtuqqhyphskktvboatbnrmayturngrvgqyclfxfaflccwmgmciacieineaiqxwoiuerfsqcuvggsmaclcokeuyjeegmndpsomtjxumkxwthlludskjxjdjnuhqnxkrjnoarnzgajlhajyynuikajoixwvkxbhcxebujyrxoeqffijyefwlbeeiusyjaubvgxthgllmbkkskqxicaqbpinugldsrzzjemdqiafdynwunouistwinveyylqparpedxixcygdtirxdqqubptimwlxraktkmyrvucvzkiuffshmncmbipzqxrmovyucnnbvdxagzzzxzmzmydkoonojlcgwltnfyocpvbpnvqeouadcdnwvtdehftjsiohxkahwhvncqmzorkponzawkumfxkwaqwtcpksmqggqtsueqxklaqruhkaatxvqftzezocjuvubrdgcehzqtaeftoneapzglcmgbrjlttmephovhxmvbwwmlggmmvjzgpclczmecggpirrgyatowsczrpsvimthwmauzotziixapyoqppjpckxqyzlzlkfcdmvohcioiffcmmaznehmgrghcfpkpmibtinycunxfkygrglxdsyfxwpxcftmnrypzmtrruxyrjcadeocpwfqnsrmlcybqvlpuwaplqufucytooscmtarzxultowpknhgy"))
