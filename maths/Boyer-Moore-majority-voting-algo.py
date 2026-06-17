# https://leetcode.com/problems/majority-element/

# TC: O(n)
# SC: O(1)
class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        c = 0
        for i in nums:
            if i == candidate:
                c += 1
            else:
                c -= 1
                if c == 0:
                    candidate = i
                    c += 1
        return candidate


# https://leetcode.com/problems/majority-element-ii/

# TC: O(n)
# SC: O(1)
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        if not nums:
            return []

        # Phase 1: Candidates aur unke Counts dhundhna
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            # 1. Agar current number candidate1 ke barabar hai
            if num == candidate1:
                count1 += 1
            # 2. Agar current number candidate2 ke barabar hai
            elif num == candidate2:
                count2 += 1
            # 3. Agar candidate1 ki jagah khali hai
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            # 4. Agar candidate2 ki jagah khali hai
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            # 5. Agar number kisi se match nahi karta, toh dono ke counts kam karein
            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Verification (pakka karna ki sach mein > n // 3 baar aaye hain ya nahi)
        result = []
        n = len(nums)

        # Candidates ki asal ginti karna
        # (list.count() function ka use karke hum ise aasani se kar sakte hain)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)

        # Dhyan rahe: candidate1 aur candidate2 alag hone chahiye, varna duplicate add ho sakta hai
        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result



# https://leetcode.com/problems/minimum-index-of-a-valid-split/description

from collections import Counter

# TC: O(n)
# SC: O(n)
class Solution:

    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Poore array ka dominant element aur uska total count dhundein
        # (Chunki sawal mein guarantee hai ki ek dominant element hai, hum Counter use kar sakte hain)
        counts = Counter(nums)
        dominant_element, total_count = counts.most_common(1)[0]

        '''
            Agar booyer moore majority voting algorithm ka use karke.

            count = 0

            dominant_element = None

            # pass 1: dominant element dhundhna

            for num in nums:

                if count == 0:
                    dominant_element = num
                    count = 1

                elif num == dominant_element:
                    count += 1

                else:
                    count -= 1

        
            # Pass 2: we can get the count of the dominant element in the entire array
        
            total_count = 0
            for num in nums:
                if num == dominant_element:
                    total_count += 1
        '''

        left_count = 0

        # Step 2: Array ko har mumkin index i par split karke check karein
        for i in range(n - 1):  # n-1 tak kyunki right part khali nahi hona chahiye
            # Agar current number dominant element hai, toh left side mein uska count badhayein
            if nums[i] == dominant_element:
                left_count += 1

            # Left side ki lambai (length) kitni hogi? -> (i + 1)
            left_len = i + 1
            # Right side ki lambai kitni bachegi? -> (n - left_len)
            right_len = n - left_len
            # Right side mein dominant element kitni baar bacha? -> (total_count - left_count)
            right_count = total_count - left_count

            # Check karein: kya yeh dono taraf aadhe se zyada (> half) hai?
            if left_count * 2 > left_len and right_count * 2 > right_len:
                return i  # Pehla valid index milte hi return kar dein

        return -1  # Agar koi valid split na mile