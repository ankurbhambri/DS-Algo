class Solution:
    def fun(self,s):
        # code here
        MOD = 10**9 + 7
        
        # Teeno patterns ke counts shuruat mein 0 hain
        a_count = 0  # For expressions of form A^i
        b_count = 0  # For expressions of form A^i B^j
        c_count = 0  # For expressions of form A^i B^j C^k
        
        for char in s:
            if char == 'a':
                # 1. a ko na lo
                # 2. a ko lo
                # 3. Yeh akela naya 'a' shuru karega
                a_count = (2 * a_count + 1) % MOD
                
            elif char == 'b':
                # 1. b ko na lo
                # 2. b ko lo
                # 3. Saare valid a wale ke piche yeh 'b' judega
                b_count = (2 * b_count + a_count) % MOD
                
            elif char == 'c':
                # 1. c ko na lo
                # 2. c ko lo
                # 3. Saare valid ab wale ke piche yeh 'c' judega
                c_count = (2 * c_count + b_count) % MOD
                
        return c_count


print(Solution().fun("abcabc"))  # Output: 7
print(Solution().fun("aaabbbccc"))  # Output: 27