# https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        sm = 0
        carry = 0
        result = []

        i = len(num1) - 1
        j = len(num2) - 1

        while i > -1 or j > -1 or carry:

            n1 = num1[i] if i > -1 else '0'
            n2 = num2[j] if j > -1 else '0'

            cur_sum = ord(n1) - ord('0') + ord(n2) - ord('0') + carry

            # remainder
            sm = cur_sum % 10

            # quotient
            carry = cur_sum // 10

            result.append(str(sm))

            i -= 1
            j -= 1

        return ''.join(result[::-1])


print(Solution().addStrings("0", "0"))      # Output: "0"
print(Solution().addStrings("11", "123"))  # Output: "134"
print(Solution().addStrings("456", "77"))  # Output: "533"
print(Solution().addStrings("999", "1"))   # Output: "1000"


# Variant: What if we get Decimal numbers

class Solution:
    def addDecimalStrings(self, num1: str, num2: str) -> str:

        nums1_parts = num1.split('.')
        nums2_parts = num2.split('.')

        def addStrings(n1, n2, carry=0):

            result = []

            i = len(n1) - 1
            j = len(n2) - 1

            while i > -1 or j > -1 or carry:

                a = n1[i] if i > -1 else '0'
                b = n2[j] if j > -1 else '0'

                cur_sum = ord(a) - ord('0') + ord(b) - ord('0') + carry

                # remainder
                sm = cur_sum % 10

                # quotient
                carry = cur_sum // 10

                result.append(str(sm))

                i -= 1
                j -= 1

            return ''.join(result[::-1])

        if len(nums1_parts[1]) != len(nums2_parts[1]):
            if len(nums1_parts[1]) > len(nums2_parts[1]):
                nums2_parts[1] += '0' * (len(nums1_parts[1]) - len(nums2_parts[1]))
            else:
                nums1_parts[1] += '0' * (len(nums2_parts[1]) - len(nums1_parts[1]))

        decimal_sum = addStrings(nums1_parts[1], nums2_parts[1])
        max_frac_len = max(len(nums1_parts[1]), len(nums2_parts[1]))

        carry = 0
        if len(decimal_sum) > max_frac_len:

            carry = int(decimal_sum[0])

            decimal_sum = decimal_sum[1:]

        integer_sum = addStrings(nums1_parts[0], nums2_parts[0], carry)

        return integer_sum + '.' + decimal_sum


print(Solution().addDecimalStrings("11.2", "123.34"))  # Output: "134.54"
print(Solution().addDecimalStrings("456.5", "77.55"))  # Output: "534.05"