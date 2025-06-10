# https://leetcode.com/problems/4sum-ii/


from collections import defaultdict

'''
    Idea: Split 4Sum into two 2Sum problems using HashMap.

    Step1: Calculate all possible sums of pairs from A and B, and store their frequencies in a dictionary.

    Step2: For each pair from C and D, check if the negation of their sum exists in the dictionary. 

    Because if A[i] + B[j] + C[k] + D[l] = 0, then we can rewrite it as A[i] + B[j] = -(C[k] + D[l]).

'''


class Solution:
    def fourSumCount(self, A, B, C, D):

        # Dictionary to store sum of pairs from A and B
        ab_sum = defaultdict(int)

        # Compute all possible sums of A[i] + B[j] and store their frequency
        for a in A:
            for b in B:
                ab_sum[a + b] += 1

        count = 0

        # Now compute all possible sums of C[k] + D[l]
        for c in C:
            for d in D:
                remain = -(c + d)
                if remain in ab_sum:
                    count += ab_sum[remain]

        return count



print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # Output: 2
print(Solution().fourSumCount([0], [0], [0], [0]))  # Output: 1
print(Solution().fourSumCount([1], [1], [1], [1]))  # Output: 1
print(Solution().fourSumCount([1, 2], [3, 4], [-1, -2], [-3, -4]))  # Output: 0
