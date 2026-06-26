# https://leetcode.com/problems/subsequence-sum-after-capping-elements/


class Solution:
    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:

        n = len(nums)

        A = sorted(nums)

        # Base case: bit 0 set hai kyunki sum 0 hamesha achievable hai
        dp = 1

        idx = 0

        answer = [False] * n

        for x in range(1, n + 1):

            # 1. Jo elements <= x hain, unse bitmask update karo
            while idx < n and A[idx] <= x:
                val = A[idx]
                # yeh ((1 << (k + 1)) - 1), k + 1 bits ka mask banata hai, jisse hum ensure karte hain ki hum sirf k tak ke sums consider kar rahe hain, control karne ke liye ki humare bitmask mein sirf k tak ke bits set ho sakein.
                dp |= (dp << val) & ((1 << (k + 1)) - 1)
                idx += 1

            # 2. Remaining elements jo > x hain unka count
            rem_elements_count = n - idx

            # 3. Aapka bataya hua mask check step
            possible = False
            for m in range(rem_elements_count + 1):

                # (m * x) ka mtlab hai ki hum m elements ko x se cap kar rahe hain, aur required_sum ka matlab hai ki humare paas kitna sum bacha hai jo hume dp mask mein check karna hai.
                required_sum = k - (m * x)

                if required_sum < 0:
                    break

                # Mask check: Agar required_sum wala bit dp me set hai
                if dp & (1 << required_sum):
                    possible = True
                    break

            answer[x - 1] = possible

        return answer


print(Solution().subsequenceSumAfterCapping([1, 2, 3, 4], 5))  # Output: [True, True, True, True]
print(Solution().subsequenceSumAfterCapping([1, 2, 3, 4], 6))  # Output: [True, True, True, True]