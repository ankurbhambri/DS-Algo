# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

'''

## Idea:

1. Hum left se ek chota chunk lenge aur right se bhi utne hi size ka chunk lenge.

2. Agar dono chunks match ho jaate hain, to hum unhe cut kar denge, apne answer me +2 add karenge (kyunki ek shuruat ka chunk mila aur ek aakhiri ka), 
aur bache hue beech ke part par yahi cheez repeat karenge.

3. Agar match nahi hote, to hum chunk ka size badhaenge jab tak match na mil jaye.

4. Agar beech me sirf ek akela part bach jata hai jo kisi se match nahi ho sakta, to answer me +1 add kar denge.


## Example: text = "ghiabcdefghi"

Step 1: Left se "g" aur Right se "i". Match nahi hue.

Step 2: Size badhao. Left se "gh" aur Right se "hi". Match nahi hue.

Step 3: Size aur badhao. Left se "ghi" aur Right se "ghi". Match ho gaye!

Answer = 2 (Humne "ghi" dono taraf se nikal diya)

Ab bachi hui string hai: "abcdef"

Step 4: "abcdef" me left se "a", "ab", "abc" check karoge, par right se kuch match nahi hoga jab tak hum pure "abcdef" ko ek single chunk na maan lein.

Answer = 2 + 1 = 3.

'''

class Solution:
    def longestDecomposition(self, text: str) -> int:
        l = ""
        r = ""
        res = 0
        n = len(text)
        for i in range(n):
            l += text[i]
            r = text[n - 1 - i] + r
            if l == r:
                l = ""
                r = ""
                res += 1
        return res


print(Solution().longestDecomposition("merchant"))
print(Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))