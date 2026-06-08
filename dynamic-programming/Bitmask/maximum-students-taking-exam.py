# https://leetcode.com/problems/maximum-students-taking-exam

from functools import cache

# TC: O(m * 2^n * 2^n) => O(m * 4^n) (m = rows, n = cols)
# SC: O(m * 2^n) (memoization ke liye)
class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:

        m = len(seats)     # Total Rows
        n = len(seats[0])  # Total Columns

        # Step 1: Har row ke liye available (not broken) seats ka mask nikal lo
        row_avail_masks = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)  # Agar seat theek hai, toh bit 1 karo
            row_avail_masks.append(mask)

        # Helper function: Yeh count karega ki ek mask mein kitne students hain (set bits)
        def count_students(mask: int) -> int:
            return bin(mask).count('1')

        # Step 2: Recursion + Memoization
        @cache
        def solve(row_idx: int, prev_row_mask: int) -> int:

            # Base Case: Agar saari rows khatam ho gayin
            if row_idx == m:
                return 0

            max_students = 0
            avail_mask = row_avail_masks[row_idx]

            # Hum is row ke liye saare possible 2^n combinations check karenge
            # (Kyunki n <= 8 hai, toh max 256 combinations)
            for curr_mask in range(1 << n):
                # 1. Check karo ki kya yeh mask seats ke hisab se valid hai?
                # (Yani student sirf available '.' seats par hi baitha ho)
                if (curr_mask & avail_mask) != curr_mask:
                    continue

                # 2. Check karo ki same row mein koi barabar mein toh nahi baitha?
                if (curr_mask & (curr_mask >> 1)) != 0:
                    continue

                # 3. Check karo ki pichli row se cheating toh nahi ho rahi?
                # Left diagonal aur Right diagonal check
                if curr_mask & (prev_row_mask << 1) != 0 or curr_mask & (prev_row_mask >> 1) != 0:
                    continue

                # Agar saari conditions pass ho gayin, toh max nikal lo
                current_seats_count = count_students(curr_mask)
                total = current_seats_count + solve(row_idx + 1, curr_mask)
                max_students = max(max_students, total)

            return max_students

        # Shuruat Row 0 se karenge, aur shuru mein prev_row_mask = 0 (koi student nahi)
        return solve(0, 0)