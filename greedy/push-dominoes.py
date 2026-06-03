# https://leetcode.com/problems/push-dominoes

from collections import deque

# TC: O(n), where n is the length of the input string, as we process each domino at most once.
# SC: O(n), where n is the length of the input string, due to the queue and the list representation of the dominoes.

class Solution(object):
    def pushDominoes(self, s):

        res = ''
        prev = 0
        s = 'L' + s + 'R'

        for curr in range(1, len(s)):

            if s[curr] == '.':
                continue

            span = curr - prev - 1

            if prev > 0:
                res += s[prev]

            if s[prev] == s[curr]:
                res += s[prev] * span

            elif s[prev] == 'L' and s[curr] == 'R':
                res += '.' * span

            else:
                res += 'R' * (span // 2) + '.' * (span % 2) + 'L' * (span // 2)

            prev = curr

        return res

print(Solution().pushDominoes("..R...L..R."))  # Output: "..RR.LL..RR."
print(Solution().pushDominoes("RR.L"))  # Output: "RR.L"
print(Solution().pushDominoes(".L.R...LR..L.."))  # Output: "LL.RR.LLRRLL.."