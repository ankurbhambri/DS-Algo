# https://leetcode.com/problems/number-of-digit-one/


'''
Tight ka matlab

tight = True
  => Ab tak jo number bana rahe ho, woh n ke prefix ke exactly equal hai.

tight = False
  => Kahin pe chhota digit le chuke ho, ab aage kuch bhi le sakte ho.

Maan lo:
  n = 345
  Digits: [3, 4, 5]
  Position 0

Hum digit choose kar rahe hain.
Allowed: 0, 1, 2, 3
  (kyunki tight=True hai aur current digit 3 hai)

Case 1: d = 3
  Humne exactly wahi digit li jo n mein hai.
    3 _ _
  Abhi bhi number equal chal raha hai.
    new_tight = True
  Formula:
    new_tight = tight and (d == limit)
              = True and (3 == 3)
              = True

Case 2: d = 2
  Humne chhota digit le liya.
    2 _ _
  Ab jo bhi aage bharenge number kabhi bhi 345 se bada nahi ho sakta.
  Example: 299 still < 345
    Toh restriction khatam.
    new_tight = False
  Formula:
    new_tight = True and (2 == 3)
              = False

Jab tight already False ho
  Maan lo pehle hi chhota digit le liya tha:
    2 _ _
  Ab current state: tight = False
  Chahe ab digit kuch bhi lo: 0..9
    tight kabhi wapas True nahi ban sakta.
  Formula:
    new_tight = False and anything
              = False

Yaad rakhne ka shortcut:
  new_tight = tight and (d == limit)
  Read it as: "Tight tabhi rahega jab pehle bhi tight tha aur maine maximum allowed digit hi choose ki."

'''


class Solution:
    def countDigitOne(self, n: int) -> int:

        memo = {}
        digits = list(map(int, str(n)))
        m = len(digits)

        def dfs(pos, count1, tight):

            if pos == m:
                return count1

            state = (pos, count1, tight)

            if state in memo:
                return memo[state]

            # yha, agar tight hai, toh hum sirf digits[pos] tak hi ja sakte hain, warna 9 tak ja sakte hain
            limit = digits[pos] if tight else 9

            ans = 0

            for d in range(limit + 1):

                # agar hum 1 choose karte hain, toh count1 badh jayega, 
                # yha hum 1 find kar rhe h isliye d == 1 condition mein h, 
                # in case 3 find kar rhe hote toh d == 3 condition hota
                new_count = count1 + (d == 1)

                # aur agar hum limit choose karte hain, toh tight bana rahega, warna tight false ho jayega

                # for example, agar n = 13 hai, toh pehle position pe hum 1 choose kar sakte hain, toh tight true rahega, 
                # lekin agar hum 0 choose karte hain, toh tight false ho jayega, kyunki ab hum 3 tak ja sakte hain

                new_tight = tight and (d == limit)

                # ab hum next position pe jayenge
                ans += dfs(pos + 1, new_count, new_tight)

            memo[state] = ans
            return ans

        return dfs(0, 0, True)


print(Solution().countDigitOne(0))   # Output: 0
print(Solution().countDigitOne(13))  # Output: 6
print(Solution().countDigitOne(100)) # Output: 21
print(Solution().countDigitOne(1000)) # Output: 301