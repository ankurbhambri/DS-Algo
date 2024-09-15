# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

"""
Idea: In this problem, we are only focusing on vowels. For each vowel encountered, we will store its state (odd or even count) up to the current index. 
We'll represent this state using binary values: 0 for an even count and 1 for an odd count.

This 0 or 1 will help us track the state of the vowels as we process the string. 
If we encounter a matching state later, we can simply subtract the index where that state first occurred and update our result.

We are only interested in the vowels "a, e, i, o, u". Each time we find a vowel, 
we toggle its state (from even to odd or vice versa). This can be done by performing a left shift based on the vowel's position in the string "aeiou". For example, 'a' is at position 0, and 'e' is at position 1. By shifting left by the corresponding position in a binary number, we can update the state.

"""

# Storing states in string format


def solution(s):

    tmp = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    stateMap = {"00000": -1}

    res = 0

    for i in range(len(s)):

        if s[i] in tmp:
            tmp[s[i]] ^= 1
            # tmp[s[i]] += 1
            # tmp[s[i]] %= 2

        val = "".join([str(i) for i in tmp.values()])

        if val in stateMap:
            prev = stateMap[val]
            res = max(res, i - prev)

        else:
            stateMap[val] = i

    return res


print(solution("eleetminicoworoep"))  # 13
print(solution("leetcodeisgreat"))  # 5
print(solution("bcbcbc"))  # 6


# Using Bit Manupulation


def solution_bit_maupulation(s):

    hm = {}
    state = 0
    hm[state] = -1
    res = 0

    for i in range(len(s)):

        if s[i] == "a":
            state = state ^ (1 << 0)

        elif s[i] == "e":
            state = state ^ (1 << 1)

        elif s[i] == "i":
            state = state ^ (1 << 2)

        elif s[i] == "o":
            state = state ^ (1 << 3)

        elif s[i] == "u":
            state = state ^ (1 << 4)

        if state in hm:
            prev = hm[state]
            res = max(res, i - prev)
        else:
            hm[state] = i

    return res
