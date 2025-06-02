# https://leetcode.com/problems/valid-word-abbreviation/description/
# https://leetcode.ca/2017-01-11-408-Valid-Word-Abbreviation/


"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

Valid abbreviations

    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)

Not valid abbreviations:

    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)

"""


def solution(word, abbr):
    w, a = 0, 0

    while w < len(word) and a < len(abbr):

        if abbr[a].isdigit():
            steps = 0

            if abbr[a] == "0":
                return False

            while a < len(abbr) and abbr[a].isdigit():

                steps = steps * 10 + int(abbr[a])
                a += 1

            w += steps

        else:
            if word[w] != abbr[a]:
                return False

            w += 1
            a += 1

    return w == len(word) and a == len(abbr)


print(solution("internationalization", "i12iz4n"))
print(solution("apple", "a2e"))
