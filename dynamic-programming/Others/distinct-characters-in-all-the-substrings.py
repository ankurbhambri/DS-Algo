# https://leetcode.com/discuss/post/1481915/amazon-oa-count-distinct-characters-in-a-gr6u/

# similar to # https://leetcode.com/problems/total-appeal-of-a-string


"""
    Given a string, return the sum of count of distinct characters in all the substrings of that string.

    Input: "test"

    Explanation: Possible substrings with distinct character count

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


# TC: O(n)
# SC: O(n)
def sum_of_distinct_counts(s: str) -> int:

    n = len(s)

    total_sum = 0

    # Track the last seen index of each character
    # Initialize all characters with -1 (meaning not seen yet)
    last_seen = {}

    for i, char in enumerate(s):

        # j is the index of the previous occurrence
        j = last_seen.get(char, -1)

        # finding uniqueness from left, before it's repeated word, like t at 3 and t at 0
        # so will take left choices from 1 to 3, which is 3 - 0 = 3
        # j is denoting the last seen index of the character
        left_choices = i - j

        # for right we are just checking how many choices we have from the current index to the end of the string
        right_choices = n - i

        # yha hum total sum me add kar rahe hain, left choices * right choices,
        # kyunki har unique character ke liye, uske left aur right ke combinations se hi unique substrings bante hain
        total_sum += left_choices * right_choices

        # Update the last seen position of the character
        last_seen[char] = i

    return total_sum


print(sum_of_distinct_counts("test")) # 19
print(sum_of_distinct_counts("abbca")) # 28
print(sum_of_distinct_counts("code")) # 20


'''
Old Solution

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

'''