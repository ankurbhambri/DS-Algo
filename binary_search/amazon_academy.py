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
    res = r

    while l <= r:

        m = (l + r) // 2
        x = 0

        for p in pages:
            x += ceil(p / m)

        if x <= days:
            res = min(res, m)
            r = m - 1

        else:
            l = m + 1

    return res


print(minimumNumberOfPages(4, [2, 3, 4, 5], 5))


"""
Code Question 2: Maximum Total Area of Rectangles

Amazon Games have introduced a new mathematical game for kids. You will be given n sticks, and the player is required to form rectangles from those sticks.

Problem Statement:

Given an array of n integers representing the lengths of the sticks, you need to create rectangles using those sticks. 
Note that each stick can be used in at most one rectangle, and to create a rectangle, you must have exactly two pairs of sticks 
with the same lengths. For example, you can create rectangles using sticks of lengths [2, 2, 5, 5] and [4, 4, 4, 4], but not with [3, 3, 5, 8]. 
The goal of the game is to maximize the total sum of areas of all the rectangles formed.

In order to make the game more interesting, you are allowed to reduce any integer by at most 1. Given the array sideLengths, 
representing the lengths of the sticks, find the maximum sum of areas of rectangles that can be formed such that each element
of the array can be used as length or breadth of at most one rectangle, and you are allowed to decrease any integer by at most 1. 
Since this number can be quite large, return the answer modulo 10^9 + 7.

Note:
- It is not required that all side lengths be used.
- a mod b represents the remainder obtained when an integer a is divided by an integer b.

Example:

Given side lengths sideLengths = [2, 6, 6, 2, 3, 5]:
- The lengths 2, 2, 6, and 6 can be used to form a rectangle of area 2 * 6 = 12.
- No other rectangles can be formed with the remaining lengths.
- The answer is 12 mod (10^9 + 7) = 12.

Function Description:
Complete the function getMaxTotalArea in the editor below.

def getMaxTotalArea(sideLengths: List[int]) -> int:

Parameters:

int sideLengths[n]: The side lengths that can be used to form rectangles.

Returns: int: The maximum total area of the rectangles that can be formed, modulo 10^9 + 7.

Constraints:

1 ≤ n ≤ 10^5
2 ≤ sideLengths[i] ≤ 10^9

Input Format for Custom Testing:

The first line contains an integer n, the size of sideLengths.
Each of the next n lines contains an integer, representing sideLengths[i].

Sample Case 0:

Sample Input:
8 -> sideLengths [] size n = 8
2 -> sideLengths = [2, 3, 3, 4, 6, 8, 8, 6]
3
3
4
6
8
8
6

Sample Output:
54

"""

import heapq


def getMaxTotalArea(sideLengths):
    MOD = 10**9 + 7

    max_heap = [-x for x in sideLengths]

    heapq.heapify(max_heap)

    ans = 0

    while len(max_heap) >= 4:

        num1 = -heapq.heappop(max_heap)
        num2 = -heapq.heappop(max_heap)
        num3 = -heapq.heappop(max_heap)
        num4 = -heapq.heappop(max_heap)

        if abs(num1 - num2) <= 1 and abs(num3 - num4) <= 1:
            ans += min(num1, num2) * min(num3, num4)

        elif abs(num1 - num2) <= 1:
            heapq.heappush(max_heap, -num1)
            heapq.heappush(max_heap, -num2)

        elif abs(num3 - num4) <= 1:
            heapq.heappush(max_heap, -num3)
            heapq.heappush(max_heap, -num4)

            if abs(num2 - num3) <= 1:
                heapq.heappush(max_heap, -num4)

        ans %= MOD

    return ans


# Sample input
sideLengths = [2, 3, 3, 4, 6, 8, 8, 6]
print(getMaxTotalArea(sideLengths))  # Expected Output: 54

# Test Case 2
sideLengths2 = [2, 2, 5, 5, 4, 4, 4, 4]
# Expected Output: 28
print(getMaxTotalArea(sideLengths2))

# Test Case 3
sideLengths3 = [2, 2, 2, 3, 3, 3, 4, 4]
# Expected Output: 16
print(getMaxTotalArea(sideLengths3))

# Test Case 4
sideLengths4 = [3, 3, 5, 8]
# Expected Output: 100
print(getMaxTotalArea(sideLengths4))

# Test Case 5
sideLengths5 = [1, 1, 1, 1, 1, 1, 1, 1]
# Expected Output: 2
print(getMaxTotalArea(sideLengths5))
