# https://leetcode.com/problems/number-of-matching-subsequences/


# TC: O(len(s) * len(word))

def solution(s, words):

    def is_subsequence(A, B):
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                j += 1
            i += 1
        return j == len(B)
    
    res = 0
    for w in words:
        if is_subsequence(s, w):
            res += 1

    return res

print(solution("abcde", ["a", "bb", "acd", "ace"]))  # True
print(solution("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))  # True


import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words):

        # Preprocess s: store all positions for each character
        positions = {}
        for i, ch in enumerate(s):
            positions.setdefault(ch, []).append(i)
        
        def is_subsequence(word):
            prev_pos = -1
            for ch in word:
                if ch not in positions:
                    return False
                pos_list = positions[ch]
                # find index in pos_list that is > prev_pos using binary search
                idx = bisect.bisect_right(pos_list, prev_pos)
                if idx == len(pos_list):
                    return False
                prev_pos = pos_list[idx]
            return True

        # Count subsequences
        return sum(is_subsequence(w) for w in words)


print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # 3
print(Solution().numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))  # 2
