'''
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

https://www.geeksforgeeks.org/problems/jumping-numbers3805/1

Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1.
All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Given a positive number X. Find the largest Jumping Number smaller than or equal to X.

Input:
X = 50
Output:
45
Explanation:
45 is the largest Jumping Number
possible for X = 50.

......12 + 11, 23 + 11, 34 + 11, 45

queue = [1.......9]

num = 1 <= X

last = num % 10

last - 1

nex_num = nums - 10 + (last - 1)

last + 1

nex_num = nums - 10 + (last + 1)

if nex_num <= x:
    add in que


q = [1, 2, 3, 10, 12, 21, 23]

'''
from collections import deque


# TC: O(# of jums <= X)
# SC: O(# of generated numbers)
class Solution:
    def jumpingNums(self, n):

        if n <= 9:
            return n

        ans = 0
        q = deque()

        for i in range(1, 10):
            q.append(i)

        while q:

            num = q.popleft()

            if num <= n:

                ans = max(ans, num)

                last = num % 10

                if last > 0:

                    next_num = num * 10 + (last - 1)

                    if next_num <= n:
                        q.append(next_num)

                if last < 9:

                    next_num = num * 10 + (last + 1)

                    if next_num <= n:
                        q.append(next_num)

        return ans


print(Solution().jumpingNums(50)) # 45
print(Solution().jumpingNums(10)) # 10
print(Solution().jumpingNums(100)) # 98