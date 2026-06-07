# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests


# TC: O(2^r * (r + N)) where r is the number of requests and N is the number of buildings.
# SC: O(n) for the indegree array which keeps track of the net transfers for


# Bitmasking + iteration over subsets approach:
class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:

        r = len(requests)
        max_ans = 0

        # Total combinations: 2^r (Agar r=16 hai, toh total_masks = 65536)
        total_masks = 1 << r  # This is equal to 2^r

        # 0 se lekar (2^r - 1) tak har ek subset (mask) ko check karo
        for mask in range(total_masks):

            # Har naye mask ke liye fresh checking register
            indegree = [0] * n
            set_bits_count = 0  # Is subset mein kitni requests picked hain

            # Mask ki har ek bit ko check karo (0 se lekar r-1 tak)
            for i in range(r):

                # Kya i-th bit '1' hai? (Yaani kya i-th request ko subset mein lena hai?)
                if (mask >> i) & 1:
                    set_bits_count += 1
                    from_b, to_b = requests[i]
                    indegree[from_b] -= 1
                    indegree[to_b] += 1

            # Ab check karo kya is subset ne saari buildings ka balance 0 kiya?
            valid = True
            for val in indegree:
                if val != 0:
                    valid = False
                    break

            # Agar balance strictly 0 hai, toh apna answer update karo
            if valid:
                max_ans = max(max_ans, set_bits_count)

        return max_ans


# Backtracking approach, much more efficient than bitmasking for this problem, Thoda Slow (Kyunki har mask ke liye r aur N dono ka loop chalna fix hai).

# TC: O(2^r * N)
# SC: O(r + N) (stack + array for indegree)
class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:

        # Har building ka net balance track karne ke liye array (ya dict)
        self.indegree = [0] * n
        self.max_res = 0

        def dfs(index, count):

            # Base Case: Jab humne saari requests ke baare mein faisla le liya
            if index == len(requests):

                # Check karo kya saari buildings ka indegree 0 hai, in case nhi h matlab yeh subset/combination valid nhi hai
                if all(b == 0 for b in self.indegree):
                    self.max_res = max(self.max_res, count)

                return

            # --- Option 1: Is request ko IGNORE kar do ---
            dfs(index + 1, count)

            # --- Option 2: Is request ko ACCEPT kar lo ---
            start, end = requests[index]
            self.indegree[start] -= 1
            self.indegree[end] += 1

            # Agli request par jao, count ko 1 badha do
            dfs(index + 1, count + 1)

            # BACKTRACK: Wapas aate waqt apna change undo karo
            self.indegree[start] += 1
            self.indegree[end] -= 1

        # 0th request se shuru karo, starting count 0 hai
        dfs(0, 0)

        return self.max_res