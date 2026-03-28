# Discussion Post - https://leetcode.com/discuss/interview-question/1481915/amazon-oa-count-distinct-characters-in-all-substrings

# Similar question - https://leetcode.com/problems/total-appeal-of-a-string/

"""
    Given a string, return the sum of count of distinct characters in all the substrings of that string.
    For example:
    Input String - "test"
    Possible substrings with distinct character count

    "t" -> 1
    "e" -> 1
    "s" -> 1
    "t" -> 1
    "te" -> 2
    "es" -> 2
    "st" -> 2
    "tes" -> 3
    "est" -> 3
    "test" -> 3
    Number of distinct chars - 1+1+1+1+2+2+2+3+3+3 = 19
    Output - 19
"""


def solution(s):

    last = {}
    res = 0
    for i,c in enumerate(s):
        last[c] = i + 1
        res += sum(last.values())
    return res

print(solution("test"))  # 19
print(solution("abbca")) # 28
print(solution("code")) # 20