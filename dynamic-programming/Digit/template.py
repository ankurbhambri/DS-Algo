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


Time Complexity Analysis:
  For an integer with n digits (where n = log₁₀(R)):
    Overall: O(n x Base x S)
    - n: number of digits (up to 18 for 64-bit integers)
    - Base: number system (typically 10 for decimal)
    - S: additional DP states (tight constraint, remainder, seen digits)
    - Result: ~10⁵ operations or less

Space Complexity Analysis:
  O(n x S) for memoization table and recursion stack
  where n = number of digits and S = number of states

'''

# mostly we got the range problem template, like count '1' in digits or '3' in digits or sum of digits must be prime etc.

# here, we are not finding solution for 0 to x, we have to find solution in a range l to r
# so, for that we find solution till r and till l - 1 like  prefix and then we subtract them to get the solution in the range l to r

def solve(x):
    
    memo = {}
    s = str(x)

    def dfs(pos, tight, cnt):

        if pos == len(s):
            return 1

        if (pos, tight, cnt) in memo:
            return memo[(pos, tight, cnt)]

        limit = int(s[pos]) if tight else 9

        ans = 0

        for d in range(limit + 1):
            
            new_cnt = cnt + (d == 1)

            new_tight = tight and (d == limit)

            ans += dfs(pos + 1, new_tight, new_cnt)

        memo[(pos, tight, cnt)] = ans
        return ans
    
    return dfs(0, True, 0)

l, r = 1, 1000
print(solve(r) - solve(l - 1)) # 1000