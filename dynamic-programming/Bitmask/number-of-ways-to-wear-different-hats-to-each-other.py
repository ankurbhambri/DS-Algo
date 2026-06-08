# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/


from linecache import cache
from collections import defaultdict


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:

        n = len(hats)
        MOD = 10**9 + 7

        target_mask = (1 << n) - 1  # Jaise agar 3 log hain toh 111 (binary) yani 7

        # Step 1: Reverse Mapping (Kaunsi hat kis-kis bande ko pasand hai)
        hat_to_people = defaultdict(list)
        for person_id, person_hats in enumerate(hats):
            for hat in person_hats:
                hat_to_people[hat].append(person_id)

        # Step 2: Recursion + Memoization using @cache
        @cache
        def solve(hat_id: int, mask: int) -> int:

            # Base Case 1: Agar sabhi logo ko hat mil gayi hai
            if mask == target_mask:
                return 1

            # Base Case 2: Agar saari 40 hats check ho gayi par sabko nahi mili
            if hat_id > 40:
                return 0

            # Choice 1: Is hat ko skip kar do, kisi ko mat do
            ways = solve(hat_id + 1, mask)

            # Choice 2: Agar yeh hat kuch log pasand karte hain, toh unhe dekar check karo
            if hat_id in hat_to_people:
                for person in hat_to_people[hat_id]:
                    # Agar is bande ke paas pehle se hat nahi hai (bit `0` hai)
                    if (mask & (1 << person)) == 0:
                        # Bande ko hat de di (bit ko `1` kar diya) aur aage badhe
                        ways += solve(hat_id + 1, mask | (1 << person))

            return ways % MOD

        # Hat 1 se start karenge aur initially mask 0 hoga
        return solve(1, 0)