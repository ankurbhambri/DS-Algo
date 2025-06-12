class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Convert to absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainder_map = {}  # Stores {remainder: position_in_result}
        fractional_part = []

        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the start index of the repeating part
                idx = remainder_map[remainder]
                fractional_part.insert(idx, "(")
                fractional_part.append(")")
                break

            remainder_map[remainder] = len(fractional_part)
            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder %= denominator

        result.extend(fractional_part)
        return "".join(result)


print(Solution().fractionToDecimal(1, 3))  # Output: "0.(3)"
print(Solution().fractionToDecimal(2, 1))  # Output: "2"
print(Solution().fractionToDecimal(4, 333))  # Output: "0.(012)"
print(Solution().fractionToDecimal(1, 6))  # Output: "0.1(6)"
print(Solution().fractionToDecimal(1, 7)) # Output: "0.(142857)"
print(Solution().fractionToDecimal(1, 2))  # Output: "0.5"
