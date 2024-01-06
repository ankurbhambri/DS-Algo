# https://leetcode.com/discuss/interview-question/1481915/amazon-oa-count-distinct-characters-in-all-substrings
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


def solution(ss):
    dd = {}
    n = len(ss)
    tmp = 1
    count = 0
    dd[ss[0]] = 1
    for i in range(n):
        tmp += 1 + i - dd.get(ss[i], 0)
        dd[ss[i]] = i + 1
        count += tmp
    return count


# Example usage
input_string = "test"
output = solution(input_string)
print("Output:", output)
