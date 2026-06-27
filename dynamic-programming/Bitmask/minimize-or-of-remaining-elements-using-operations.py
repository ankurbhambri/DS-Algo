# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        # 'mask' store karega ki hum abhi tak kaun-kaun si bits ko 
        # successfully ZERO (khatam) karne mein kaamyab rahe hain.
        mask = 0

        # Loop chalega 29th bit se lekar 0th bit tak (Badi bit se Choti bit).
        # Kyunki badi bit ko 0 banane se final OR ka answer sabse zyada kam hoga.
        for bit in range(29, -1, -1):

            # andRes batayega ki current kharab elements ka aapas mein AND result kya chal raha hai.
            andRes = 0

            # opsNeeded batayega ki is current bit ko pure array se hatane ke liye kitne adjacent AND lage.
            opsNeeded = 0

            # Greedy step: Maan lete hain ki yeh current bit bhi 0 ban sakti hai.
            # Ise mask mein temporarily '1' set kar dete hain check karne ke liye.
            mask |= 1 << bit

            # Pure array ke elements par traverse karenge yeh check karne ke liye 
            # ki kya hum is bit ko poore array se mukt (free) kar sakte hain?
            for x in nums:

                if andRes != 0:
                    # Agar pichla kharab element chal raha hai, to uske adjacent (padosi)
                    # element 'x' ko bhi isme merge (AND) karo aur operation count badhao.
                    andRes &= x
                    opsNeeded += 1

                elif x & mask != 0:
                    # Agar 'andRes' 0 tha, lekin humein ek naya aisa element mila jisme 
                    # mask wali kharab bits present hain (x & mask != 0), 
                    # to hum yahan se ek naya merging chunk shuru karenge.
                    andRes = x & mask

            # Loop khatam hone ke baad, agar aakhiri chunk abhi bhi 0 nahi ho paya (andRes != 0),
            # to use khatam karne ke liye ek aur operation lagana padega (pichle element ke saath).
            if andRes != 0:
                opsNeeded += 1

            # AGAR BUDGET SE BAHAR HO GAYE:
            # Agar is bit ko remove karne ke liye operations hamari limit 'k' se zyada lag rahe hain,
            # to iska matlab yeh bit 0 nahi ban sakti. Ise mask se wapas hata do (Rollback).
            if opsNeeded > k:
                mask -= 1 << bit

        # FINAL ANSWER:
        # 'mask' mein wo saari bits '1' hain jinhe humne successfully 0 bana diya.
        # Hamein return karna hai final minimum OR value (yani jo bits 0 NAHI ho payin).
        # Isiliye full 30-bits mask ((1 << 30) - 1) mein se hamare 'mask' ko minus (invert) kar denge.
        return (1 << 30) - 1 - mask