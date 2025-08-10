# https://leetcode.com/problems/lexicographical-numbers

# Question: Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.


# TC: O(n)
# SC: O(log n)

# DFS

class Solution:
    def lexicalOrder(self, n: int):
        res = []

        def helper(curr):

            if curr > n:
                return

            res.append(curr)

            for i in range(10):

                next_num = curr * 10 + i

                # This `break` statement will discard the rest of the loop since we are generating numbers out of bound order, and it will go back to the previous number
                # like start 1 will create 10 will create 100 exceed boundary discard it, go back to 10, and again 10 will create 101 discard it, go back to 1, still 1 creations are not exceeding boundary
                # it will continue else it will also dicarded and will shift to next number 2....
                # we can use return as well which will also work the same in this conntext.
                if next_num > n:
                    break

                helper(next_num)

        for i in range(1, 10):
            helper(i)

        return res


print(Solution().lexicalOrder(13))  # [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().lexicalOrder(20))  # [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]


# TC: O(n)
# SC: O(1)

# Iterative

class Solution:
    def lexicalOrder(self, n: int):

        res = []
        curr = 1

        # Generate numbers from 1 to n
        for _ in range(n):
            res.append(curr)

            # If multiplying the current number by 10 is within the limit, do it
            if curr * 10 <= n:
                curr *= 10
            else:
                # Adjust the current number by moving up one digit
                while curr % 10 == 9 or curr >= n:
                    curr //= 10  # Remove the last digit
                curr += 1  # Increment the number

        return res


print(Solution().lexicalOrder(13))  # [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().lexicalOrder(20))  # [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
