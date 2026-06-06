# https://leetcode.com/problems/largest-multiple-of-three/

'''
Case 1: rem = 1

    Need to reduce digit sum by 1 (mod 3).

Either:

    remove one digit with remainder 1
    OR remove two digits with remainder 2

Choose the option that removes fewer/smaller digits.

Case 2: rem = 2

    Need to reduce digit sum by 2 (mod 3).

Either:

    remove one digit with remainder 2
    OR remove two digits with remainder 1


Sort digits ascending first.

Why? Because when removing digits, we want to remove the smallest possible digits.

After removals, sort descending to form the largest number.
'''

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:

        digits.sort()

        rem1 = []
        rem2 = []

        total = sum(digits)

        for i, d in enumerate(digits):

            if d % 3 == 1:
                rem1.append(i)

            elif d % 3 == 2:
                rem2.append(i)

        remove = set()

        r = total % 3

        if r == 1:

            if rem1:
                remove.add(rem1[0])

            elif len(rem2) >= 2:
                remove.add(rem2[0])
                remove.add(rem2[1])

            else:
                return ""

        elif r == 2:

            if rem2:
                remove.add(rem2[0])

            elif len(rem1) >= 2:
                remove.add(rem1[0])
                remove.add(rem1[1])

            else:
                return ""

        ans = []
        for i, d in enumerate(digits):
            if i not in remove:
                ans.append(str(d))

        ans.reverse()  # descending order

        if not ans:
            return ""

        # handle all zeros
        if ans[0] == '0':
            return "0"

        return "".join(ans)


print(Solution().largestMultipleOfThree([8, 1, 9]))
print(Solution().largestMultipleOfThree([8, 6, 7, 1, 0]))