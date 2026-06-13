# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string


# TC: O(n)
# SC: O(n)
class Solution:
    def uniqueLetterString(self, s: str) -> int:

        n = len(s)
        total_sum = 0

        # Har character ke saare positions (indices) ko store karenge
        # Jaise 't': [0, 3], 'e': [1], 's': [2]
        positions = {}
        for i, char in enumerate(s):
            if char not in positions:
                positions[char] = []
            positions[char].append(i)

        # Ab har character ke har index par contribution nikaalenge
        for char, indices in positions.items():

            for k in range(len(indices)):

                i = indices[k]

                # Agar pehla occurrence hai toh prev = -1, nahi toh pichla index
                prev = indices[k - 1] if k > 0 else -1

                # Agar aakhri occurrence hai toh next = n, nahi toh agla index
                next_idx = indices[k + 1] if k < len(indices) - 1 else n

                # Formula apply karenge
                total_sum += (i - prev) * (next_idx - i)

        return total_sum


print(Solution().uniqueLetterString("ABC")) # 10
print(Solution().uniqueLetterString("LEETCODE")) # 92