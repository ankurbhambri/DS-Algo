class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)
        b = ""
        for i in str(a[2:]):
            if i == "0":
                b += "1"
            else:
                b += "0"
        return int(b, 2)
