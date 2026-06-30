# https://leetcode.com/problems/count-complete-substrings/

# TC: O(n * 26), SC: O(26) ~ O(1)
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:

        # --- STEP 2: Ek valid segment ke andar substrings count karne ka function ---
        def count_for_segment(s: str) -> int:

            ans = 0
            n = len(s)

            # 'u' represent karta hai unique characters ka count (max 26 hi ho sakte hain)
            for u in range(1, 27):

                window_len = u * k

                # Agar required window size segment ki length se bada hai, toh aage check karne ki zaroorat nahi
                if window_len > n:
                    break

                freq = {}          # Window ke andar characters ka count rakhne ke liye
                count_with_k = 0   # Kitne characters ki frequency EXACTLY 'k' ho chuki hai

                # Fixed-size sliding window shuru karte hain
                for i in range(n):

                    # 1. Right side se naya character window mein enter hua
                    char_in = s[i]
                    freq[char_in] = freq.get(char_in, 0) + 1

                    # Agar frequency exactly k ho gayi, toh hamari condition meet hui
                    if freq[char_in] == k:
                        count_with_k += 1

                    # Agar frequency k se badh gayi, toh condition break ho gayi
                    elif freq[char_in] == k + 1:
                        count_with_k -= 1

                    # 2. Agar window ka size fix limit (window_len) se bada ho jaye, 
                    # toh Left side se character ko window se bahar nikalna padega
                    if i >= window_len:

                        char_out = s[i - window_len]

                        # Agar bahar nikalne se pehle woh exactly k tha, toh ab count kam hoga
                        if freq[char_out] == k:
                            count_with_k -= 1

                        # Agar pehle k+1 tha, toh ab ghat kar exactly k ho jayega (yaani valid)
                        elif freq[char_out] == k + 1:
                            count_with_k += 1

                        freq[char_out] -= 1

                    # 3. Validation Check: Kya current window ek complete substring hai?
                    # Window poori tarah banti hai tabhi jab index >= window_len - 1 ho
                    if i >= window_len - 1 and count_with_k == u:
                        ans += 1

            return ans

        # --- STEP 1: Main logic - String ko valid segments mein todna ---

        start = 0
        total_count = 0
        n = len(word)

        for i in range(1, n + 1):
            # Agar string khatam ho gayi ya adjacent characters ka gap 2 se bada mila
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                segment = word[start:i]       # Tukda nikal liya
                total_count += count_for_segment(segment)  # Is tukde ka answer nikala
                start = i                     # Naye segment ka start pointer update kiya

        return total_count


print(Solution().countCompleteSubstrings("abcde", 1))  # Output: 15
print(Solution().countCompleteSubstrings("aabbcc", 2))  # Output: 6