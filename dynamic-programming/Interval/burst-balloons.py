# https://leetcode.com/problems/burst-balloons

# similar to https://leetcode.com/problems/minimum-score-triangulation-of-polygon

'''
Idea

1. Problem Kya Hai? (In Simple Words)
   Hume ek array diya hai nums jisme balloons ke points hain. Agar hum kisi i-th balloon ko 
   burst (phodte) karte hain, toh hume points milte hain:

   Points = nums[i-1] * nums[i] * nums[i+1]
   
   Twist: Jab ek balloon burst ho jata hai, toh uske left aur right waale balloons ek 
   doosre ke padosi (neighbors) ban jaate hain! Aur agar boundary ke baahar jaana pade, 
   toh wahan hum imaginary 1 maan lete hain.
   
   Hume saare balloons ko aise order mein phodna hai ki Maximum Points milein.

2. Dimag Lagao: Ulti Soch (The Reverse Trick)
   
   Agar aap seedha sochoge ki "Pehle kaun sa balloon phodu?", toh fass jaoge. Kyunki ek 
   balloon phodte hi baaki saare balloons ke padosi badal jayenge, aur sub-problems aapas 
   mein mix ho jayengi (dependent ho jayengi).

   Iska Hack kya hai? Ulta socho! Hum sochenge ki is poore interval [l, r] mein sabse 
   aakhiri (Last) balloon kaun sa burst hoga.

   Maan lo mid waala balloon sabse aakhiri mein burst hota hai:
   
   - Agar mid sabse aakhiri hai, toh iska matlab mid ke left waale saare balloons (l se mid-1) aur,
    right waale saare balloons (mid+1 se r) pehle hi burst ho chuke hain!
   
   - Agar woh pehle hi gayab ho chuke hain, toh ab mid ke immediate padosi kaun bache?,
    Interval ke ekdum baahar waale elements, yaani l - 1 aur r + 1!

   Toh mid ko sabse aakhiri mein phodna ka point kitna milega? - Points = nums[l-1] * nums[mid] * nums[r+1]

3. DP Formula (Recurrence Relation)

    - dp[l][r] = dp[l][mid-1] + dp[mid+1][r] + (nums[l-1] * nums[mid] * nums[r+1])

    - dp[l][mid-1]: Left waale balloons ko phodney ka max profit.

    - dp[mid+1][r]: Right waale balloons ko phodney ka max profit.

    - nums[l-1] * nums[mid] * nums[r+1]: Is pure interval mein aakhiri bache mid balloon ko phodney ka profit.
'''

# TC: O(n^3)
# SC: O(n^2)
class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        # Boundary handles karne ke liye shuru aur end mein 1 add kar do
        nums = [1] + nums + [1]

        n = len(nums)

        # dp[n][n] ki table banayi, sabme shuru mein 0
        dp = [[0] * n for _ in range(n)]

        # length 1 se shuru hogi (kyunki ek single balloon bhi burst ho sakta hai)
        # padding hatakar real elements n-2 hain, toh length max n-2 tak jayegi
        for length in range(1, n - 1):

            for l in range(1, n - length):

                r = l + length - 1

                # Is interval [l, r] ke liye max coins dhoondenge
                for mid in range(l, r + 1):

                    # Formula laga diya
                    coins = (dp[l][mid - 1] + dp[mid + 1][r] + (nums[l - 1] * nums[mid] * nums[r + 1]))

                    dp[l][r] = max(dp[l][r], coins)

        # Hamara real array 1 se lekar n-2 tak tha (padding ke bina)
        return dp[1][n - 2]