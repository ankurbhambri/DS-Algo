# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/


class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:

        n = len(tasks)
        
        # Target mask jab saare tasks ho jayein (e.g., agar n=3, toh 111 in binary)
        target_mask = (1 << n) - 1
        
        memo = {}

        def dp(mask: int, curr_time: int) -> int:

            # Base Case: Saare tasks khatam
            if mask == target_mask:
                return 0
            
            if (mask, curr_time) in memo:
                return memo[(mask, curr_time)]
            
            res = float('inf')
            
            # Har ek task ko check karo
            for i in range(n):
                # Agar i-th task abhi tak nahi kiya hai
                if not (mask & (1 << i)):
                    # Option 1: Agar yeh task current session mein fit ho sakta hai
                    if curr_time + tasks[i] <= sessionTime:
                        res = min(res, dp(mask | (1 << i), curr_time + tasks[i]))
                    else:
                        # Option 2: Is task ke liye ek naya session start karo
                        # Naya session start ho raha hai isliye +1 kiya
                        res = min(res, 1 + dp(mask | (1 << i), tasks[i]))

            memo[(mask, curr_time)] = res
            return res

        # Shuruat mein mask 0 hoga aur current session ka time bhi 0 hoga.
        # Pehla task automatic naya session start kar dega (1 + ...), isliye hum +1 add karke bhejte hain
        # Ya fir direct 1 + dp(0, 0) samajh lo kyunki pehla session toh chahiye hi.
        return 1 + dp(0, 0)