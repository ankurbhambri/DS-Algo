# https://leetcode.com/problems/koko-eating-bananas/

import math


def minEatingSpeed(piles, h):

    l, r = 1, max(piles)

    while l <= r:

        m = (l + r) // 2
        hours = 0

        for p in piles:
            hours += math.ceil(p / m)

        if hours <= h:

            r = m - 1
        else:
            l = m + 1

    return l


""" 
Similar problem

Given an int array wood representing the length of n pieces of wood and an int k. 
It is required to cut these pieces of wood such that more or equal to k pieces of the same length len are cut. What is the longest len you can get?

Example 1:

Input: wood = [5, 9, 7], k = 3
Output: 5
Explanation: 
5 -> 5
9 -> 5 + 4
7 -> 5 + 2

Example 2:

Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation: 
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3
Example 3:

Input: wood = [1, 2, 3], k = 7
Output: 0
Explanation: We cannot make it.
Example 4:

Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long, however we can't cut it into 7 pieces if any piece is 115 long.

"""


def cutWood(wood, k):

    def countPieces(wood, length):
        count = 0
        for piece in wood:
            count += piece // length
        return count

    left, right = 1, max(wood)
    while left <= right:

        mid = left + (right - left) // 2
        pieces = countPieces(wood, mid)

        if pieces >= k:
            left = mid + 1
        else:
            right = mid - 1

    return right

"""
A student is preparing for a test from Amazon Academy for a scholarship.
The student is required to completely read n chapters for the test where the ith chapter has pages[i] number of pages. 
The chapters are read in increasing order of the index.
Each day the student can either read till the end of a chapter or at most x pages, whichever is minimum. 
The number of pages remaining to read decreases by x in the latter case.

For example, if pages = [5, 3, 4] and x = 4,

• Day 1: The student reads 4 pages of the first chapter - pages remaining = [1, 3, 4]
• Day 2: The student can only read till the end of the first chapter - pages remaining = [0, 3, 4]
• Day 3: The student can read either till the end of the chapter or x = 4 pages, since 3 < 4, the student reads till the end of the chapter 2 - pages remaining = [0, 0, 4]
• Day 4: The student reads all the 4 pages of the last chapter - pages remaining - [0, 0, 0]

The test will be given in days number of days from now.
Find the minimum number of pages, x, which the student should read each day to finish all pages of all chapters within days number of days. 
If it is not possible to finish these chapters
in days number of days, return -1.

Note: In one day, the student cannot read pages of more than one chapter. Thus, if a chapter finishes, the next chapter starts only on the next day even if the number of pages read is less than x.

Example :-
There are n = 3 chapters, pages = [2, 4, 3], and days = 4.
Number of pages read each day, x = 3

After Day 1: 0 4 3

After Day 2: 0 1 3

After Day 3: 0 0 3

After Day 4: 0 0 0

Thus, in 4 days, the student can read all pages of all chapters, and finish. If x is less than 3, it is impossible to read all chapters in 4 days. Thus, the minimum number of pages read each day is 3.

Function Description

Complete the function minimumNumberOfPages in the editor below.

minimumNumberOfPages has the following parameters:
int pages[n]: the number of pages in each chapter
int days. the maximum number of days

Returns

int: the minimum number of pages to be read each day, or -1 if it is not possible to finish

Constraints
• 1 ≤ n ≤ 105
• 1 ≤ days ≤ 109
• 1 ≤ pages[i] ≤ 104
▾ Input Format For Custom Testing

The first line contains an integer, n, the number of elements in pages.
Each line i of the n subsequent lines (where 0 <i<n) contains an integer, pages[i]. The last line contains an integer, days.

Sample Case 0

4 -> pages[] size n = 4
2 -> pages = [2, 3, 4, 5]
3
4
5
5 -> days 5

Sample Output: 4

"""

from math import ceil


def minimumNumberOfPages(n, pages, days):

    l, r = 1, len(pages)

    while l <= r:

        m = (l + r) // 2
        x = 0

        for p in pages:
            x += ceil(p / m)

        if x <= days:

            r = m - 1

        else:
            l = m + 1

    return l


print(minimumNumberOfPages(4, [2, 3, 4, 5], 5))
