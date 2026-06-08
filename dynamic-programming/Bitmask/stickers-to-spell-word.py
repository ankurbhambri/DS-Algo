# https://leetcode.com/problems/stickers-to-spell-word/


from functools import lru_cache


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:

        n = len(target)
        target_mask = (1 << n) - 1

        # Har sticker ke characters ka count pehle se nikal kar rakh lete hain
        # sticker_counts = [{"w": 1, "i": 1, "t": 1, "h": 1}, ...]
        sticker_counts = []
        for sticker in stickers:
            count = {}
            for char in sticker:
                count[char] = count.get(char, 0) + 1
            sticker_counts.append(count)

        @lru_cache(None)
        def solve(mask):

            # Base Case: Agar saare characters mil gaye, toh 0 sticker aur chahiye
            if mask == target_mask:
                return 0

            # Pehla character dundo target ka jo abhi tak mask mein filled nahi hai (bit state 0 hai)
            # iski help se hum vo stricker find karenge jisme character h and usko pura exhaust karenge
            first_blank_idx = -1
            for i in range(n):
                if not (mask & (1 << i)):
                    first_blank_idx = i
                    break

            char_to_match = target[first_blank_idx]
            res = float('inf')

            # Saare stickers try karo
            for sticker_count in sticker_counts:

                # OPTIMIZATION: Sirf wahi sticker lo jisme yeh missing character ho
                if char_to_match not in sticker_count:
                    continue

                # sticker_count ki ek copy banao taaki use modify kar sakein is state ke liye
                available_chars = sticker_count.copy()
                next_mask = mask

                # Check karo yeh sticker target ke bache hue kaun-kaun se characters ko fill kar sakta hai
                for i in range(n):

                    # Agar i-th bit abhi fill nahi hai
                    if not (next_mask & (1 << i)):

                        char = target[i]

                        # Agar sticker ke paas woh character bacha hai, toh use kar lo
                        if available_chars.get(char, 0) > 0:
                            available_chars[char] -= 1
                            next_mask |= (1 << i) # Is character ki bit ko 1 (filled) kar do

                # Agar is sticker ko lene se mask mein koi badlav aaya (change hua), toh recursive call karo
                if next_mask != mask:
                    res = min(res, 1 + solve(next_mask))

            return res

        ans = solve(0)
        return ans if ans != float('inf') else -1


print(Solution().minStickers(["notice","possible"], "basicbasic"))  # Output: -1
print(Solution().minStickers(["with","example","science"], "thehat"))  # Output: 3